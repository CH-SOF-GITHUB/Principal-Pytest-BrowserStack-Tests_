from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators.locators import DuckDuckGoResultLocators
from locators.locators import DuckDuckGoSearchLocators


class LocatorMode:
    XPATH = "xpath"
    CSS_SELECTOR = "cssSelector"
    NAME = "name"
    ID = "id"
    TAG_NAME = "tagName"
    CLASS_NAME = "className"
    LINK_TEXT = "linkText"
    PARTIAL_LINK_TEXT = "partialLinkText"


class DuckDuckGoSearchPage:

    # constructor of class
    def __init__(self, driver):
        self.driver = driver

    # Methods of class
    def search(self, Text):
        wait = WebDriverWait(self.driver, 10)
        search_field = wait.until(EC.visibility_of_element_located(DuckDuckGoSearchLocators.search_input_locator))
        search_field.send_keys(Text)
        search_field.send_keys(Keys.RETURN)

    def search_by_button(self, Text):
        search_field = self.driver.find_element(*DuckDuckGoSearchLocators.search_input_locator)
        search_field.send_keys(Text)
        search_btn = self.driver.find_element(*DuckDuckGoSearchLocators.search_button_locator)
        search_btn.click()

    def enter_input_search(self, Text):
        search_field = self.driver.find_element(*DuckDuckGoSearchLocators.search_input_locator)
        search_field.send_keys(Text)

    def wait_for_auto_complete_suggestions_visibility(self, waitTime, locatorMode, Locator):
        element = None
        if locatorMode == LocatorMode.ID:
            element = WebDriverWait(self.driver, waitTime).until(EC.visibility_of_element_located((By.ID, Locator)))
        elif locatorMode == LocatorMode.NAME:
            element = WebDriverWait(self.driver, waitTime).until(EC.visibility_of_element_located((By.NAME, Locator)))
        elif locatorMode == LocatorMode.XPATH:
            element = WebDriverWait(self.driver, waitTime).until(EC.visibility_of_element_located((By.XPATH, Locator)))
        elif locatorMode == LocatorMode.CSS_SELECTOR:
            element = WebDriverWait(self.driver, waitTime).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, Locator)))
        elif locatorMode == LocatorMode.CLASS_NAME:
            element = WebDriverWait(self.driver, waitTime).until(
                EC.visibility_of_element_located((By.CLASS_NAME, Locator)))
        else:
            raise Exception("Strategy of wait By Different Locators visibility not supported")
        return element

    def list_of_suggestions(self, waitTime, locatorMode, Locator):
        options = None
        if locatorMode == LocatorMode.LINK_TEXT:
            options = WebDriverWait(self.driver, waitTime).until(
                EC.visibility_of_all_elements_located((By.LINK_TEXT, Locator)))
        elif locatorMode == LocatorMode.PARTIAL_LINK_TEXT:
            options = WebDriverWait(self.driver, waitTime).until(
                EC.visibility_of_all_elements_located((By.PARTIAL_LINK_TEXT, Locator)))
        elif locatorMode == LocatorMode.CLASS_NAME:
            options = WebDriverWait(self.driver, waitTime).until(
                EC.visibility_of_all_elements_located((By.CLASS_NAME, Locator)))
        else:
            raise Exception("Strategy Link TEXT of wait visibility not supported")
        return options