"""
Creating a testing suite
Example web app: https://opensource-demo.orangehrmlive.com

TC (Test Case) definitions
"""
import time

import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Locators import LoginPageLocators


@pytest.fixture
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('window-size=1920x1080')
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    time.sleep(3)
    yield driver
    driver.quit()


def test_TC_L_001(driver):
    driver.get('https://opensource-demo.orangehrmlive.com')
    # 1. Verify Login panel exists
    wait = WebDriverWait(driver, 20)
    Login_panel = wait.until(EC.visibility_of_element_located(LoginPageLocators.Login_panel_locator))
    assert Login_panel.text == "Login"
    # 2. Verify Username input filed exists
    Username_input_field = wait.until(EC.visibility_of_element_located(LoginPageLocators.Username_locator))
    assert Username_input_field.get_attribute("placeholder") == "Username"
    # 3. Verify Password field exists
    Password_field = wait.until(EC.visibility_of_element_located(LoginPageLocators.Password_locator))
    assert Password_field.get_attribute("placeholder") == "Password"
    # 4. Verify Login button exists and enabled for clicking
    LoginButton = wait.until(EC.element_to_be_clickable(LoginPageLocators.Login_button_locator))
    assert LoginButton.text == "Login"
