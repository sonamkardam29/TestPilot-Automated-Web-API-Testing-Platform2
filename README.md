# TestPilot - Automated Web & API Testing Platform

A portfolio SDET project: API automation, Selenium UI automation, Pytest, Page Object Model, SQLite validation, test execution history, HTML reports, screenshots, and CI.

## Architecture
```
Frontend UI (HTML/CSS/JavaScript)
        |
     FastAPI
        |
  SQLite (SQLAlchemy)
        |
Test Execution Engine
        |
      Pytest
     /      \
Selenium   Requests
   |          |
  UI         API
     \      /
      Results
         |
    HTML Report
         |
  GitHub Actions
```

## Stack
Python | FastAPI | Pytest | Selenium | Requests | SQLite | SQLAlchemy | HTML/CSS/JavaScript | GitHub Actions

The application under test is a small Task Manager (Flask + SQLite) in `app/`, so the project is fully self-contained.

## Run
```powershell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python run.py
```
Open http://127.0.0.1:8000 (Google Chrome must be installed for Selenium).

## Run tests manually
```powershell
pytest tests/api -v
pytest tests/ui -v
pytest -v --html=reports/full-report.html --self-contained-html
```
Use `pytest -m smoke` for the quick suite. Set `HEADLESS=0` to watch the browser.

## Main UI
Dashboard - Run Tests - Test Cases - Test Runs - Results - Settings

Every navigation item has its own view. The Run Tests page starts real Pytest suites through the FastAPI execution service. Results and run history are persisted in SQLite via SQLAlchemy. Each run has a downloadable HTML report, and failed UI tests save a screenshot to `reports/screenshots/`.

## Project structure
```
app/            application under test (REST API + web UI)
dashboard/      FastAPI execution service + dashboard UI
tests/api       API tests (Requests)
tests/ui        UI tests (Selenium, Page Object Model in tests/ui/pages)
tests/db        database tests
tests/unit      DSA unit tests
utils/          API client, DSA toolkit
postman/        Postman collection
docs/           test plan, SDLC notes, AI usage notes
.github/workflows/ci.yml   GitHub Actions
run.py          starts TestPilot
```

## Interview summary
"TestPilot is an end-to-end SDET project where I built API and UI automation with Pytest, Requests and Selenium. I used Page Object Model and fixtures for maintainability, SQLite with SQLAlchemy for test-run and result persistence, FastAPI for the execution and reporting layer, and GitHub Actions for CI."
