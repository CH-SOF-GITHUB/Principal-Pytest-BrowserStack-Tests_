from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.home import HomePageDemoQa
from utils.locators import RegisterPageLocators


class RegisterPageDemoQA(HomePageDemoQa):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)
        self.open_page("https://demoqa.com/register")

    def get_register_page_title(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(
            EC.visibility_of_element_located(RegisterPageLocators.Register_to_Book_Store_title_locator))
        return element.text

    def enter_firstname(self, firstname):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(RegisterPageLocators.FirstName_input_locator))
        element.send_keys(firstname)

    def enter_lastname(self, lastname):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(RegisterPageLocators.LastName_input_locator))
        element.send_keys(lastname)

    def enter_username(self, username):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(RegisterPageLocators.UserName_input_locator))
        element.send_keys(username)

    def enter_password(self, pwd):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(RegisterPageLocators.Password_input_locator))
        element.send_keys(pwd)

    def click_recaptcha_checkbox(self):
        # --- Switch to iframe using WebElement ---
        iframe = self.driver.find_element(*RegisterPageLocators.RECAPTCHA_IFRAME_LOCATOR)
        self.driver.switch_to.frame(iframe)
        recaptcha_to_click = self.driver.find_element(*RegisterPageLocators.RECAPTCHA_CHECKBOX_LOCATOR)
        recaptcha_to_click.click()
        print("\n++++Clicked the reCAPTCHA checkbox.++++")

    def click_register_button(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(RegisterPageLocators.button_register_locator))
        element.click()

    def click_back_to_login(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(RegisterPageLocators.button_back_to_login_locator))
        element.click()
