from selenium.webdriver.common.by import By
from .base_page import BasePage
class DashboardPage(BasePage):
    TITLE=(By.ID,"title"); CARDS=(By.CLASS_NAME,"cards")
    def loaded(self): return self.wait.until(lambda d:d.find_element(*self.TITLE).text=="Dashboard")
    def cards_visible(self): return self.wait.until(lambda d:d.find_element(*self.CARDS).is_displayed())
