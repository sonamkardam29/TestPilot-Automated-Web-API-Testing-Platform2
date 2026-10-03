# 🚀 TestPilot - Automated Web & API Testing Platform

TestPilot is an end-to-end **SDET automation project** designed to demonstrate practical Software Testing and Test Automation concepts through API automation, UI automation, test execution, database validation, reporting, screenshots, and Continuous Integration.

The project combines **Pytest, Requests, Selenium, FastAPI, SQLite, SQLAlchemy, Page Object Model, HTML reporting, and GitHub Actions** into a single automation platform.

---

# 🎯 Project Objective

The main objective of TestPilot is to build a practical automation framework that can:

- Automate REST API testing
- Automate web UI testing
- Execute test suites from a central dashboard
- Maintain reusable test fixtures
- Apply Page Object Model for UI automation
- Store test cases and execution results
- Maintain test execution history
- Generate HTML test reports
- Capture UI automation artifacts
- Run tests automatically through CI
- Provide a simple interface for monitoring automation results

The project is designed to demonstrate how an SDET can build and manage an automation solution instead of writing only individual test scripts.

---

# 🎯 Project Goal

The goal of TestPilot is to create a **centralized test automation platform** where API and UI test suites can be executed and monitored from one place.

Instead of manually running separate Pytest commands, the user can use the TestPilot dashboard to trigger:

```text
API Test Suite
UI Test Suite
Full Test Suite
```

The system executes the selected suite, stores the execution information, generates reports, and makes the results available through the dashboard.

---

# 💡 Problem Statement

In a traditional automation project, testers may have:

- Separate API test scripts
- Separate UI test scripts
- Different commands for different test suites
- Test results stored only in terminal output
- No centralized execution history
- No simple dashboard for monitoring executions

TestPilot addresses these problems by providing a single interface for test execution and result monitoring.

```text
Before TestPilot

API Tests  ──> Terminal
UI Tests   ──> Terminal
Reports    ──> Separate Files
History    ──> Not Centralized


With TestPilot

                TestPilot Dashboard
                       |
             +---------+---------+
             |                   |
          API Tests           UI Tests
             |                   |
             +---------+---------+
                       |
                    Pytest
                       |
                 Test Results
                       |
             +---------+---------+
             |                   |
          SQLite             HTML Report
             |
       Execution History
```

---

# 🏗️ Architecture

```text
                         TESTPILOT
                  AUTOMATION PLATFORM
                           |
                           v
              +--------------------------+
              |     Dashboard UI         |
              |   HTML / CSS / JS        |
              +------------+-------------+
                           |
                           v
              +--------------------------+
              |         FastAPI          |
              | Backend + Execution API  |
              +------------+-------------+
                           |
                           v
              +--------------------------+
              |   Test Execution Engine  |
              +------------+-------------+
                           |
                           v
                       Pytest
                     /       \
                    /         \
                   v           v
              Requests      Selenium
                  |             |
                  v             v
              API Tests      UI Tests
                                |
                                v
                         Page Object Model
                           /          \
                          v            v
                     BasePage    DashboardPage
                           |
                           v
                    Test Execution
                           |
              +------------+-------------+
              |                          |
              v                          v
       SQLite Database              HTML Reports
       SQLAlchemy ORM               pytest-html
              |                          |
              v                          v
       Test Cases                  Test Reports
       Test Runs
       Test Results
              |
              v
        Execution History
              |
              v
       GitHub Actions CI
```

---

# 🔄 Complete Test Execution Flow

When the user starts a test from the dashboard:

```text
User
 |
 | Select Test Suite
 |
 v
TestPilot Dashboard
 |
 v
FastAPI Backend
 |
 v
Create Test Run
 |
 v
Test Execution Engine
 |
 v
Pytest
 |
 +-----------------------+
 |                       |
 v                       v
API Automation       UI Automation
 |                       |
 v                       v
Requests               Selenium
 |                       |
 v                       v
API Tests             Page Objects
 |                       |
 +-----------+-----------+
             |
             v
       Test Results
             |
       +-----+-----+
       |           |
       v           v
    SQLite      HTML Report
       |
       v
Execution History
       |
       v
Dashboard
```

---

# 🧰 Tech Stack

| Technology        | Purpose                                |
| ----------------- | -------------------------------------- |
| Python            | Core programming language              |
| FastAPI           | Backend API and test execution service |
| Pytest            | Test automation framework              |
| Requests          | REST API automation                    |
| Selenium          | Web UI automation                      |
| Page Object Model | Maintainable UI automation             |
| SQLite            | Lightweight database                   |
| SQLAlchemy        | Database ORM                           |
| HTML              | Dashboard structure                    |
| CSS               | Dashboard styling                      |
| JavaScript        | Dashboard functionality                |
| pytest-html       | HTML test reporting                    |
| GitHub Actions    | Continuous Integration                 |
| Git               | Version control                        |
| GitHub            | Source code hosting                    |

---

# ✨ Key Features

## 1. API Automation

API automation is implemented using:

```text
Python
+
Requests
+
Pytest
```

API tests validate:

- HTTP status codes
- API responses
- JSON response data
- Health endpoint
- Test case endpoints
- Summary endpoint
- Invalid request handling
- API behaviour

---

## 2. UI Automation

UI automation is implemented using:

```text
Selenium WebDriver
+
Pytest
+
Page Object Model
```

The UI automation validates the TestPilot dashboard and its important pages.

Example areas:

```text
Dashboard
Test Cases
Test Runs
Results
Navigation
```

---

## 3. Page Object Model

The UI automation follows the Page Object Model design pattern.

```text
pages/
│
├── base_page.py
└── dashboard_page.py
```

### BasePage

Contains reusable browser operations such as:

- Open page
- Find elements
- Click elements
- Get element text
- Common Selenium operations

### DashboardPage

Contains dashboard-specific:

- Locators
- Navigation methods
- Dashboard actions
- Page validation

This keeps test logic separate from UI locator logic and makes the automation easier to maintain.

---

# 🧪 Pytest Framework

Pytest is used as the main automation framework.

The project uses:

- Fixtures
- Assertions
- Test markers
- Test modules
- Test discovery
- HTML reporting

Common fixtures are maintained in:

```text
conftest.py
```

Typical fixtures include:

```text
base_url
api_session
driver
```

---

# 🗂️ Project Structure

```text
TestPilot-Automated-Testing-Platform/
│
├── .github/
│   └── workflows/
│       └── tests.yml
│
├── app/
│   ├── __init__.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   ├── seed.py
│   │
│   ├── static/
│   │   ├── app.js
│   │   └── styles.css
│   │
│   └── templates/
│       └── index.html
│
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   └── dashboard_page.py
│
├── tests/
│   ├── api/
│   │   ├── test_cases.py
│   │   ├── test_health.py
│   │   └── test_summary.py
│   │
│   └── ui/
│       └── test_dashboard.py
│
├── reports/
│   └── .gitkeep
│
├── screenshots/
│   └── .gitkeep
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── run.py
├── .gitignore
└── README.md
```

---

# 📁 Important Folders

## app/

Contains the FastAPI application.

```text
app/
├── main.py
├── database.py
├── models.py
├── seed.py
├── static/
└── templates/
```

### main.py

Responsible for:

- FastAPI application
- API endpoints
- Dashboard serving
- Test execution
- Report access

### database.py

Responsible for:

- SQLite connection
- SQLAlchemy engine
- Database session

### models.py

Contains SQLAlchemy database models.

### seed.py

Used for initializing sample test-case data.

### static/

Contains frontend assets:

```text
app.js
styles.css
```

### templates/

Contains the dashboard UI:

```text
index.html
```

---

## pages/

Contains Page Object Model classes.

```text
pages/
├── base_page.py
└── dashboard_page.py
```

These classes provide reusable Selenium operations for UI testing.

---

## tests/

Contains automated tests.

```text
tests/
├── api/
└── ui/
```

### tests/api/

Contains API automation using Requests and Pytest.

```text
test_cases.py
test_health.py
test_summary.py
```

### tests/ui/

Contains Selenium UI automation.

```text
test_dashboard.py
```

---

## reports/

Stores generated HTML test reports.

Example:

```text
reports/
├── api-report.html
├── ui-report.html
└── full-report.html
```

---

## screenshots/

Stores screenshots generated during UI automation or failure analysis.

```text
screenshots/
```

---

## .github/workflows/

Contains GitHub Actions CI configuration.

```text
.github/
└── workflows/
    └── tests.yml
```

---

# 🗄️ Database Architecture

TestPilot uses:

```text
SQLite
+
SQLAlchemy
```

SQLite provides lightweight local persistence while SQLAlchemy provides the ORM layer.

The database stores information related to:

```text
Test Cases
Test Runs
Test Results
```

---

# 📊 Test Case Data

A test case contains information such as:

```text
Test ID
Test Name
Test Type
Endpoint
Description
Status
```

Example:

```text
TC-001
Health API Test
API
/health
Verify health endpoint
Active
```

---

# 📈 Test Run Data

Each execution creates a test run.

A test run contains:

```text
Run ID
Suite
Status
Total Tests
Passed Tests
Failed Tests
Duration
Report Path
Start Time
```

Example:

```text
Run ID       : 12
Suite        : API
Status       : Passed
Total        : 3
Passed       : 3
Failed       : 0
Duration     : 2.41 sec
```

---

# 📋 Test Result Data

Individual test results contain information such as:

```text
Test Name
Test Type
Status
Duration
Message
Run ID
Created Time
```

This allows TestPilot to maintain execution-level information instead of relying only on terminal output.

---

# 🌐 Main API Endpoints

| Method | Endpoint                | Description                              |
| ------ | ----------------------- | ---------------------------------------- |
| GET    | `/health`               | Checks whether the backend is running    |
| GET    | `/api/summary`          | Total cases, runs, passed, failed, pass % |
| GET    | `/api/test-cases`       | Returns available automation test cases  |
| GET    | `/api/test-cases/{id}`  | Returns details of a specific test case  |
| GET    | `/api/runs`             | Returns previous test execution history  |
| GET    | `/api/runs/{run_id}`    | Returns details of a specific execution  |
| GET    | `/api/results`          | Returns individual test results          |
| POST   | `/api/execute/api`      | Starts the API automation suite          |
| POST   | `/api/execute/ui`       | Starts the Selenium UI automation suite  |
| POST   | `/api/execute/full`     | Runs the complete automation suite       |
| GET    | `/api/reports`          | Returns available generated reports      |

---

# 🖥️ Dashboard

The TestPilot dashboard provides different sections for managing and monitoring automation.

```text
Dashboard
│
├── Overview
│
├── Run Tests
│
├── Test Cases
│
├── Test Runs
│
├── Results
│
└── Settings
```

## Overview

Provides an overview of automation execution:

```text
Total Test Cases
Total Test Runs
Passed Tests
Failed Tests
Pass Percentage
Recent Runs
```

## Run Tests

Allows the user to start:

```text
API Test Suite
UI Test Suite
Full Test Suite
```

The request is sent to FastAPI, which starts the appropriate Pytest command.

## Test Cases

Displays available automation test cases:

```text
Test ID
Test Name
Type
Endpoint
Description
Status
```

## Test Runs

Displays execution history:

```text
Run ID
Suite
Status
Total
Passed
Failed
Duration
Report
```

## Results

Displays individual test execution results, so the user can see which specific tests passed or failed.

## Settings

Provides information about the automation environment:

```text
Automation Framework : Pytest
API Automation       : Requests
UI Automation        : Selenium
Backend              : FastAPI
Database             : SQLite
ORM                  : SQLAlchemy
Reporting            : pytest-html
CI                   : GitHub Actions
```

---

# 💻 How to Start the Project in VS Code

## Step 1 - Open VS Code

Open Visual Studio Code.

## Step 2 - Open the Project Folder

```text
File
 ↓
Open Folder
 ↓
TestPilot-Automated-Testing-Platform
```

The project explorer should show:

```text
app/
pages/
tests/
reports/
screenshots/
.github/
requirements.txt
run.py
pytest.ini
```

## Step 3 - Open VS Code Terminal

```text
Terminal
 ↓
New Terminal
```

## Step 4 - Create Virtual Environment

```powershell
python -m venv venv
```

## Step 5 - Activate Virtual Environment

For Windows PowerShell:

```powershell
venv\Scripts\activate
```

If activated successfully, the terminal will show something similar to:

```text
(venv) PS C:\...\TestPilot-Automated-Testing-Platform>
```

## Step 6 - Install Dependencies

```powershell
pip install -r requirements.txt
```

This installs the required packages such as:

```text
FastAPI
Uvicorn
Pytest
Requests
Selenium
SQLAlchemy
pytest-html
```

## Step 7 - Start TestPilot

```powershell
python run.py
```

The application will start locally. Open the following URL in Google Chrome:

```text
http://127.0.0.1:8000
```

Chrome is required for Selenium UI automation.

---

# 🧪 Running Tests from VS Code

Run all tests:

```powershell
pytest -v
```

Run API tests:

```powershell
pytest tests/api -v
```

Run UI tests:

```powershell
pytest tests/ui -v
```

Generate HTML report:

```powershell
pytest -v --html=reports/full-report.html --self-contained-html
```

---

# 🏷️ Pytest Markers

The project organizes tests using Pytest markers:

```text
api
ui
smoke
```

```powershell
pytest -m api -v
pytest -m ui -v
pytest -m smoke -v
```

---

# 🌐 API Automation Example

```python
@pytest.mark.api
def test_health_endpoint(api_session, base_url):
    response = api_session.get(base_url + "/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"
```

The test:

```text
1. Sends GET request
2. Receives API response
3. Validates HTTP status
4. Validates response body
```

---

# 🖥️ UI Automation Example

```python
@pytest.mark.ui
def test_dashboard_loads(driver, base_url):
    page = DashboardPage(driver)

    page.open(base_url)

    assert page.loaded()
```

The test:

```text
1. Starts Chrome WebDriver
2. Opens TestPilot
3. Uses DashboardPage
4. Performs UI interaction
5. Validates dashboard
```

---

# 🧱 Page Object Model Flow

```text
UI Test
   |
   v
DashboardPage
   |
   v
BasePage
   |
   v
Selenium WebDriver
   |
   v
Browser
```

The benefit is that Selenium-specific implementation remains inside page classes instead of being duplicated throughout test files.

---

# 📊 HTML Reporting

TestPilot uses `pytest-html` to generate test execution reports.

```powershell
pytest -v --html=reports/full-report.html --self-contained-html
```

The generated report contains:

```text
Test Name
Test Status
Execution Time
Test Result
Summary
```

---

# 📸 Screenshots

The project maintains a dedicated `screenshots/` directory for UI automation artifacts.

Screenshots are useful for:

- Debugging failed UI tests
- Understanding browser state
- Failure analysis
- Automation evidence

---

# 🔄 CI/CD with GitHub Actions

```text
Developer Push
      |
      v
GitHub Repository
      |
      v
GitHub Actions
      |
      v
Setup Python
      |
      v
Install Dependencies
      |
      v
Run Tests
      |
      v
Generate Reports
      |
      v
CI Result
```

Workflow file:

```text
.github/workflows/tests.yml
```

This allows automated testing without manually running Pytest after every code change.

---

# ❓ Why These Technologies?

**SQLite** - lightweight, no separate database server, easy to configure, and well suited for a portfolio automation project with local execution history.

**SQLAlchemy** - provides an ORM layer so the application works with Python models instead of raw SQL.

```text
FastAPI
   |
SQLAlchemy
   |
SQLite
```

**FastAPI** - provides REST API development, request handling, database integration, test execution endpoints, report endpoints, dashboard serving, and automatic API documentation. It is the bridge between the dashboard and the Pytest execution engine.

**Pytest** - simple test structure, fixtures, assertions, markers, test discovery, plugins, HTML reporting, and easy CI integration.

**Selenium** - browser-based UI automation:

```text
Open Browser
      ↓
Open Application
      ↓
Interact with UI
      ↓
Validate Elements
      ↓
Capture Test Result
```

**Requests** - REST API automation with `GET`, `POST`, `PUT`, and `DELETE` requests and response validation.

**Page Object Model** - improves maintainability, reusability, readability, and scalability by centralizing locators and page actions in page classes.

---

# 🧪 Testing Strategy

```text
                    TestPilot
                       |
          +------------+------------+
          |                         |
      API Testing              UI Testing
          |                         |
      Requests                  Selenium
          |                         |
       Pytest                 Page Objects
          |                         |
          +------------+------------+
                       |
                    Results
                       |
              Database + Reports
```

## API Tests (`tests/api/`)

- API health validation
- Test-case endpoint validation
- Summary endpoint validation
- Response validation

## UI Tests (`tests/ui/`)

- Dashboard loading
- UI navigation
- Dashboard validation
- Browser-based workflows

## Smoke Testing

Smoke tests give a quick validation of the application's important functionality, so major failures are caught before the complete suite runs.

```powershell
pytest -m smoke -v
```

---

# 🧠 SDET Concepts Demonstrated

```text
Test Automation
API Testing
UI Testing
Selenium
Pytest
Fixtures
Assertions
Page Object Model
REST APIs
HTTP Status Codes
JSON Validation
Database Testing
SQLAlchemy
SQLite
Test Execution
Test Result Persistence
HTML Reporting
Screenshots
CI/CD
GitHub Actions
Git
GitHub
```

---

# 📈 Future Improvements

- Parallel test execution
- More API test scenarios
- More UI Page Objects
- Advanced test filtering
- Test scheduling
- Email/Slack notifications
- Docker-based execution
- More detailed test analytics
- Additional browser support
- Advanced failure diagnostics

---

# 🎓 What I Learned From This Project

- Designing an automation framework
- Writing API automation using Requests
- Writing UI automation using Selenium
- Using Pytest fixtures
- Applying Page Object Model
- Building REST APIs using FastAPI
- Working with SQLite and SQLAlchemy
- Persisting test execution results
- Generating HTML reports
- Managing automation artifacts
- Integrating automated tests with GitHub Actions
- Structuring a real-world SDET project

---

# 🗣️ Interview Explanation

### Short Version

> TestPilot is an end-to-end SDET automation platform where I implemented API and UI automation using Pytest, Requests, and Selenium. I used Page Object Model and fixtures for maintainable UI automation. FastAPI acts as the backend and test execution layer, while SQLite with SQLAlchemy stores test cases, test runs, and test results. I also integrated HTML reporting and GitHub Actions for CI.

### Detailed Version

> I built TestPilot to demonstrate a complete SDET automation workflow instead of only individual test scripts. The project has a FastAPI-based dashboard that allows users to trigger API, UI, or full test suites. Pytest is used as the main automation framework, Requests is used for API testing, and Selenium is used for UI automation. For UI maintainability, I implemented the Page Object Model using reusable page classes. Test execution information is stored in SQLite using SQLAlchemy, and pytest-html is used to generate reports. Finally, GitHub Actions is used to execute the automation suite as part of CI.

---

# 💼 Resume Description

### TestPilot - Automated Web & API Testing Platform

- Built an end-to-end **SDET automation platform** using Python, Pytest, Selenium, Requests, FastAPI, SQLite, and SQLAlchemy.
- Implemented **API and UI automation** with Pytest, Selenium WebDriver, reusable fixtures, and Page Object Model.
- Developed FastAPI-based test execution endpoints to trigger **API, UI, and full automation suites** and maintain test execution history.
- Integrated **SQLite/SQLAlchemy persistence, pytest-html reporting, screenshots, and GitHub Actions CI** for automated test execution and reporting.

---

# 📌 GitHub Repository

[https://github.com/sonamkardam29/TestPilot-Automated-Testing-Platform](https://github.com/sonamkardam29/TestPilot-Automated-Testing-Platform)

---

# 👩‍💻 Author

**Sonam Kardam**

B.Tech - Computer Science Engineering (AIML)

GitHub: [https://github.com/sonamkardam29](https://github.com/sonamkardam29)

---

# ⭐ Project Summary

```text
TestPilot
    |
    +-- API Automation
    |      |
    |      +-- Requests
    |      +-- Pytest
    |
    +-- UI Automation
    |      |
    |      +-- Selenium
    |      +-- Page Object Model
    |
    +-- Backend
    |      |
    |      +-- FastAPI
    |
    +-- Database
    |      |
    |      +-- SQLite
    |      +-- SQLAlchemy
    |
    +-- Reporting
    |      |
    |      +-- pytest-html
    |      +-- Screenshots
    |
    +-- CI/CD
           |
           +-- GitHub Actions
```

---

# 🚀 Final Workflow

```text
Write Test
    ↓
Pytest
    ↓
API / UI Automation
    ↓
Test Execution
    ↓
Validate Results
    ↓
Store Results in SQLite
    ↓
Generate HTML Report
    ↓
Display Results on Dashboard
    ↓
Run Automatically through GitHub Actions
```

**TestPilot demonstrates a complete practical SDET workflow from writing and executing automated tests to storing, reporting, and continuously running test results.**
