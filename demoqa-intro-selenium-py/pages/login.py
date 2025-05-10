from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.home import HomePageDemoQa
from utils.locators import LoginPageLocators


class LoginPageDemoQA(HomePageDemoQa):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)
        self.open_page("https://demoqa.com/login")

    def enter_username(self, username):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(LoginPageLocators.UserName_input_locator))
        element.send_keys(username)
        print(f"\nSTEP 1: username '{username}' entered")

    def enter_password(self, password):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(LoginPageLocators.Password_input_locator))
        element.send_keys(password)
        print(f"\nSTEP 2: password '{password}' entered")

    def click_login_button(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(LoginPageLocators.button_login_locator))
        element.click()
        print("\nSTEP 3: login button clicked !")

    # return the error messages
    def error_message(self):
        error_message = self.driver.find_element(*LoginPageLocators.error_message_locator)
        return error_message

    def get_error_message(self):
        element = self.error_message()
        error_message = element.text
        return error_message

    def inputs_error_message(self):
        wait = WebDriverWait(self.driver, 10)
        elements = wait.until(
            EC.visibility_of_all_elements_located(LoginPageLocators.input_error_message_locator))
        return elements
