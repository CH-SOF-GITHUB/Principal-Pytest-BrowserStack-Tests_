from selenium.webdriver.common.by import By


class LoginPageLocators:
    Login_panel_locator = (By.CLASS_NAME, "orangehrm-login-title")
    Username_locator = (By.NAME, "username")
    Password_locator = (By.NAME, "password")
    Login_button_locator = (By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button")
