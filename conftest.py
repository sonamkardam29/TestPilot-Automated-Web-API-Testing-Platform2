import os, pytest, requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
BASE_URL=os.getenv("TESTPILOT_URL","http://127.0.0.1:8000")
@pytest.fixture
def base_url(): return BASE_URL
@pytest.fixture
def api_session():
    s=requests.Session(); yield s; s.close()
@pytest.fixture
def driver():
    o=Options(); o.add_argument("--headless=new"); o.add_argument("--window-size=1440,1000"); o.add_argument("--no-sandbox")
    d=webdriver.Chrome(options=o); yield d; d.quit()
