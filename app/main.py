import subprocess, sys, time, threading
from pathlib import Path
from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from .database import Base, engine, get_db, SessionLocal
from .models import TestCase, TestRun, TestResult
from .seed import seed

BASE = Path(__file__).resolve().parent.parent
REPORTS = BASE / "reports"
SCREENSHOTS = BASE / "screenshots"
REPORTS.mkdir(exist_ok=True); SCREENSHOTS.mkdir(exist_ok=True)
Base.metadata.create_all(bind=engine); seed()

app = FastAPI(title="TestPilot API", version="2.0")
app.mount("/static", StaticFiles(directory=Path(__file__).parent/"static"), name="static")

@app.get("/", response_class=HTMLResponse)
def home():
    return (Path(__file__).parent/"templates/index.html").read_text(encoding="utf-8")

@app.get("/health")
def health(): return {"status":"healthy","service":"testpilot-api"}

@app.get("/api/summary")
def summary(db: Session=Depends(get_db)):
    runs=db.query(TestRun).all()
    total=sum(x.total for x in runs); passed=sum(x.passed for x in runs); failed=sum(x.failed for x in runs)
    return {"test_cases":db.query(TestCase).count(),"test_runs":len(runs),"passed":passed,"failed":failed,
            "pass_percentage":round(passed*100/total) if total else 0}

@app.get("/api/test-cases")
def cases(db: Session=Depends(get_db)): return db.query(TestCase).order_by(TestCase.id).all()

@app.get("/api/runs")
def runs(db: Session=Depends(get_db)): return db.query(TestRun).order_by(TestRun.id.desc()).all()

@app.get("/api/runs/{run_id}")
def run_detail(run_id:int, db:Session=Depends(get_db)):
    run=db.query(TestRun).filter(TestRun.id==run_id).first()
    if not run: raise HTTPException(404,"Run not found")
    results=db.query(TestResult).filter(TestResult.run_id==run_id).all()
    return {"run":run,"results":results}

@app.get("/api/results")
def results(db:Session=Depends(get_db)): return db.query(TestResult).order_by(TestResult.id.desc()).all()

def execute_suite(run_id, suite, cmd, report_name):
    start=time.time()
    result=subprocess.run(cmd, cwd=BASE, capture_output=True, text=True)
    duration=round(time.time()-start,2)
    output=(result.stdout or "")+(result.stderr or "")
    passed=output.count(" passed"); failed=output.count(" failed")
    if passed==0 and result.returncode==0: passed=1
    total=passed+failed
    status="Passed" if result.returncode==0 else "Failed"
    db=SessionLocal()
    try:
        run=db.query(TestRun).filter(TestRun.id==run_id).first()
        run.status=status; run.total=total; run.passed=passed; run.failed=failed; run.duration=duration
        run.report=f"reports/{report_name}"
        db.commit()
        db.add(TestResult(run_id=run_id,test_name=f"{suite} execution",test_type="SUITE",
                          status=status,duration=duration,message=output[-700:].replace("\n"," ")))
        db.commit()
    finally: db.close()

@app.post("/api/execute/{suite}")
def execute(suite:str, db:Session=Depends(get_db)):
    mapping={"api":("API Tests",[sys.executable,"-m","pytest","tests/api","-q","--html=reports/api-report.html","--self-contained-html"],"api-report.html"),
             "ui":("UI Tests",[sys.executable,"-m","pytest","tests/ui","-q","--html=reports/ui-report.html","--self-contained-html"],"ui-report.html"),
             "full":("Full Suite",[sys.executable,"-m","pytest","-q","--html=reports/full-report.html","--self-contained-html"],"full-report.html")}
    if suite not in mapping: raise HTTPException(400,"Unknown suite")
    name,cmd,report=mapping[suite]
    run=TestRun(suite=name,status="Running",started_at=__import__("datetime").datetime.utcnow())
    db.add(run); db.commit(); db.refresh(run)
    threading.Thread(target=execute_suite,args=(run.id,name,cmd,report),daemon=True).start()
    return {"run_id":run.id,"status":"Running","suite":name}

@app.get("/api/reports")
def reports():
    return [{"name":p.name,"url":f"/reports/{p.name}","size":p.stat().st_size} for p in REPORTS.glob("*.html")]

app.mount("/reports",StaticFiles(directory=REPORTS),name="reports")
