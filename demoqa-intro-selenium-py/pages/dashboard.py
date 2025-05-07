from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utils.locators import DashboardPageLocators


class DashboardPageDemoQA:

    # constructor
    def __init__(self, driver):
        self.driver = driver

    # return the current value of UserName
    def dashboard_username(self):
        wait = WebDriverWait(self.driver, 10)
        value = wait.until(EC.visibility_of_element_located(DashboardPageLocators.dashboard_username_locator))
        return value.text

    # return the current url after loading page of dashboard
    def change_current_url_to_dashboard(self, new_url):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.url_to_be(new_url))