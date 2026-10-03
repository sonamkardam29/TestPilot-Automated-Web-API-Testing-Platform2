from .database import Base, engine, SessionLocal
from .models import TestCase, TestRun, TestResult

def seed():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        if db.query(TestCase).count() == 0:
            db.add_all([
                TestCase(name="Health Check", test_type="API", endpoint="/health", description="Validate service health"),
                TestCase(name="Get Test Cases", test_type="API", endpoint="/api/test-cases", description="Validate test-case response"),
                TestCase(name="Invalid Test Case", test_type="API", endpoint="/api/test-cases/99999", description="Validate 404 handling"),
                TestCase(name="Summary Contract", test_type="API", endpoint="/api/summary", description="Validate dashboard summary contract"),
                TestCase(name="Dashboard Loads", test_type="UI", endpoint="/", description="Validate dashboard page"),
                TestCase(name="KPI Cards Visible", test_type="UI", endpoint="/", description="Validate KPI cards"),
                TestCase(name="Recent Runs Visible", test_type="UI", endpoint="/", description="Validate run table"),
            ])
            db.commit()
        if db.query(TestRun).count() == 0:
            runs = [
                TestRun(suite="Full Suite", status="Passed", total=7, passed=7, failed=0, duration=3.42, report="reports/full-report.html"),
                TestRun(suite="API Tests", status="Passed", total=4, passed=4, failed=0, duration=1.08, report="reports/api-report.html"),
                TestRun(suite="UI Tests", status="Passed", total=3, passed=3, failed=0, duration=2.31, report="reports/ui-report.html"),
            ]
            db.add_all(runs)
            db.commit()
    finally:
        db.close()
