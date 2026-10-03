import pytest
from pages.dashboard_page import DashboardPage
@pytest.mark.ui
def test_dashboard_loads(driver,base_url):
    p=DashboardPage(driver); p.open(base_url); assert p.loaded()
@pytest.mark.ui
def test_dashboard_cards_visible(driver,base_url):
    p=DashboardPage(driver); p.open(base_url); assert p.cards_visible()
@pytest.mark.ui
def test_sidebar_navigation_views(driver,base_url):
    p=DashboardPage(driver); p.open(base_url+"#test-cases")
    assert p.wait.until(lambda d:"Test Case Repository" in d.page_source)
    p.open(base_url+"#results")
    assert p.wait.until(lambda d:"Test Results" in d.page_source)
