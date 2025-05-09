import time

from pytest_bdd import given, when, then, scenarios
from selenium.webdriver.common.by import By

# initilize a driver from seleniumbase in instance
# driver = Driver()

# Scenarios
scenarios(
    'C:\\Users\\chaker\PycharmProjects\\pytest-browserstack\\demoqa-intro-selenium-py\\testsBdd\\features\\CheckLogin.feature')
# scenarios('features/CheckLogin.feature')
# constants
DEMO_QA_LOGIN_PAGE = "https://demoqa.com/login"


@given("i open login page")
def step_impl(driver):
    driver.get(DEMO_QA_LOGIN_PAGE)
    driver.implicitly_wait(10)
    driver.maximize_window()
    print("\nSTEP 1: demoqa login page opened\n")


@when("i enter username value")
def step_impl(driver):
    username_field = driver.find_element(By.ID, "userName")
    username_field.send_keys("ch_demoqa")
    print("STEP 2: username value entered\n")


@when("i enter password value")
def step_impl(driver):
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("Admin1234!")
    print("STEP 3: password value entered\n")


@when("i click in login button")
def step_impl(driver):
    # scroll in to login button element
    driver.execute_script("window.scrollTo(0, scrollY + 200)")
    login_button = driver.find_element(By.XPATH, "//*[@id='login']")
    login_button.click()
    print("STEP 4: login button clicked\n")


# wait for 5 s for load page response
time.sleep(5)

@then("navigate to profile page and success login")
def step_impl(driver):
    current_username = driver.find_element(By.ID, "userName-value")
    assert current_username.text == "ch_demoqa"
    print("\nResult: Login and navigate to profile page passed")
