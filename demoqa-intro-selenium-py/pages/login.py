from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.home import HomePageDemoQa
from utils.locators import LoginPageLocators


class LoginPageDemoQA(HomePageDemoQa):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)
        self.open_page(url="https://demoqa.com/login")

    def enter_username(self, username):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(LoginPageLocators.UserName_input_locator))
        element.send_keys(username)
        print(f"\nusername {username} entered")

    def enter_password(self, password):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(LoginPageLocators.Password_input_locator))
        element.send_keys(password)
        print(f"\npassword {password} entered")

    def click_login_button(self):
        element = self.driver.find_element(*LoginPageLocators.button_login_locator)
        element.click()
        print("\nlogin button clicked !")
