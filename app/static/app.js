const app=document.getElementById("app"), title=document.getElementById("title"), crumb=document.getElementById("crumb");
const esc=s=>String(s??"").replace(/[&<>"']/g,m=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#039;"}[m]));
const get=async u=>(await fetch(u)).json();

function shell(kpis){return `<div class="cards">${kpis.map(x=>`<div class="card"><small>${x[0]}</small><b>${x[1]}</b><span>${x[2]}</span></div>`).join("")}</div>`}
function table(headers,rows){return `<div class="panel table"><table><thead><tr>${headers.map(h=>`<th>${h}</th>`).join("")}</tr></thead><tbody>${rows.join("")}</tbody></table></div>`}
function badge(s){return `<span class="badge ${String(s).toLowerCase()}">${esc(s)}</span>`}

async function dashboard(){
 const s=await get("/api/summary"), r=await get("/api/runs");
 app.innerHTML=shell([["Test Cases",s.test_cases,"Active"],["Test Runs",s.test_runs,"Execution history"],["Passed",s.passed,"Across recorded runs"],["Failed",s.failed,"Across recorded runs"],["Pass Rate",s.pass_percentage+"%","Automation quality"]]);
 app.innerHTML+=`<div class="grid2"><section class="panel"><h3>Execution Overview</h3><div class="bars"><i style="height:${Math.max(15,s.pass_percentage)}%"></i><i style="height:${Math.max(8,100-s.pass_percentage)}%"></i></div><div class="legend">Passed <span></span> Failed</div></section><section><div class="panel"><div class="head"><h3>Recent Runs</h3><a href="#test-runs">View all →</a></div>${table(["ID","Suite","Status","Pass","Fail"],r.slice(0,5).map(x=>`<tr><td>#${x.id}</td><td>${esc(x.suite)}</td><td>${badge(x.status)}</td><td>${x.passed}</td><td>${x.failed}</td></tr>`))}</div></section></div>`;
}
async function runTests(){
 app.innerHTML=`<div class="hero"><div><span class="eyebrow">TEST EXECUTION</span><h2>Run automated test suites</h2><p>Execute the real Pytest API, UI or full regression suite from this dashboard.</p></div></div>
 <div class="suitecards">${[["api","API Tests","Requests + FastAPI validation","☁"],["ui","UI Tests","Selenium + Page Object Model","▣"],["full","Full Suite","API + UI regression","▰"]].map(x=>`<button class="suite" onclick="startRun('${x[0]}')"><strong>${x[3]}</strong><h3>${x[1]}</h3><p>${x[2]}</p><span>Run suite →</span></button>`).join("")}</div>
 <div id="runmsg"></div><div class="panel"><h3>How execution works</h3><div class="steps"><span>1. Select suite</span><span>2. FastAPI starts Pytest</span><span>3. Results stored in SQLite</span><span>4. HTML report generated</span></div></div>`;
}
async function startRun(suite){
 document.getElementById("runmsg").innerHTML=`<div class="notice">⏳ Test execution started. Results are being collected...</div>`;
 const x=await fetch("/api/execute/"+suite,{method:"POST"}).then(r=>r.json());
 setTimeout(()=>location.hash="test-runs",800);
}
async function cases(){
 const c=await get("/api/test-cases");
 title.textContent="Test Cases";
 app.innerHTML=`<div class="toolbar"><div><h2>Test Case Repository</h2><p>Automated scenarios covered by the framework.</p></div><input id="search" placeholder="Search test cases..." oninput="filterCases()"></div>
 <div id="caseTable">${table(["ID","Test Case","Type","Endpoint","Description","Status"],c.map(x=>`<tr><td>TC-${String(x.id).padStart(3,"0")}</td><td><b>${esc(x.name)}</b></td><td>${badge(x.test_type)}</td><td><code>${esc(x.endpoint)}</code></td><td>${esc(x.description)}</td><td>${badge(x.status)}</td></tr>`))}</div>`;
 window.caseData=c;
}
function filterCases(){let q=document.getElementById("search").value.toLowerCase();let c=window.caseData.filter(x=>(x.name+x.endpoint+x.test_type).toLowerCase().includes(q));document.getElementById("caseTable").innerHTML=table(["ID","Test Case","Type","Endpoint","Description","Status"],c.map(x=>`<tr><td>TC-${String(x.id).padStart(3,"0")}</td><td><b>${esc(x.name)}</b></td><td>${badge(x.test_type)}</td><td><code>${esc(x.endpoint)}</code></td><td>${esc(x.description)}</td><td>${badge(x.status)}</td></tr>`))}
async function runs(){
 const r=await get("/api/runs"); title.textContent="Test Runs";
 app.innerHTML=`<div class="toolbar"><div><h2>Execution History</h2><p>Every suite execution is persisted in SQLite.</p></div><a class="primary" href="#run-tests">+ New Run</a></div>${table(["Run","Suite","Status","Total","Passed","Failed","Duration","Report"],r.map(x=>`<tr><td>#${x.id}</td><td><b>${esc(x.suite)}</b></td><td>${badge(x.status)}</td><td>${x.total}</td><td>${x.passed}</td><td>${x.failed}</td><td>${x.duration}s</td><td>${x.report?`<a href="/${x.report}" target="_blank">Open report ↗</a>`:"—"}</td></tr>`))}`;
}
async function results(){
 const r=await get("/api/results"); title.textContent="Results";
 app.innerHTML=`<div class="toolbar"><div><h2>Test Results</h2><p>Individual automation outcomes and execution details.</p></div><span class="pill">${r.length} results</span></div>${table(["Test","Type","Status","Duration","Details"],r.map(x=>`<tr><td><b>${esc(x.test_name)}</b></td><td>${badge(x.test_type)}</td><td>${badge(x.status)}</td><td>${x.duration}s</td><td class="detail">${esc(x.message)}</td></tr>`))}`;
}
function settings(){title.textContent="Settings";app.innerHTML=`<div class="panel settings"><h2>TestPilot Configuration</h2><div class="setting"><b>Execution Engine</b><span>Pytest</span></div><div class="setting"><b>UI Automation</b><span>Selenium WebDriver</span></div><div class="setting"><b>API Automation</b><span>Requests</span></div><div class="setting"><b>Database</b><span>SQLite + SQLAlchemy</span></div><div class="setting"><b>CI</b><span>GitHub Actions</span></div></div>`}
async function route(){
 let r=location.hash.slice(1)||"dashboard";document.querySelectorAll("nav a").forEach(a=>a.classList.toggle("active",a.dataset.route===r));
 ({dashboard, "run-tests":runTests, "test-cases":cases, "test-runs":runs, results, settings}[r]||dashboard)();
 title.textContent={"dashboard":"Dashboard","run-tests":"Run Tests","test-cases":"Test Cases","test-runs":"Test Runs","results":"Results","settings":"Settings"}[r]||"Dashboard";crumb.textContent=title.textContent;
}
window.addEventListener("hashchange",route);route();
