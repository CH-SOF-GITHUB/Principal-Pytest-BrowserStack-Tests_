from selenium.webdriver.common.by import By


class RegisterPageLocators(object):
    Register_to_Book_Store_title_locator = (By.XPATH, '//*[@id="userForm"]/div[1]/h4')
    FirstName_input_locator = (By.ID, 'firstname')
    LastName_input_locator = (By.ID, 'lastname')
    UserName_input_locator = (By.ID, 'userName')
    Password_input_locator = (By.ID, 'password')
    button_register_locator = (By.ID, 'register')
    button_back_to_login_locator = (By.ID, 'gotologin')
    # Locator for the reCAPTCHA iframe
    RECAPTCHA_IFRAME_LOCATOR = (By.XPATH, "//*[@id='g-recaptcha']/div/div/iframe")
    # Locator for the reCAPTCHA checkbox INSIDE the iframe
    RECAPTCHA_CHECKBOX_LOCATOR = (By.CSS_SELECTOR, "div.recaptcha-checkbox-border")


class LoginPageLocators(object):
    UserName_input_locator = (By.ID, 'userName')
    Password_input_locator = (By.ID, 'password')
    button_login_locator = (By.XPATH, '//*[@id="login"]')
