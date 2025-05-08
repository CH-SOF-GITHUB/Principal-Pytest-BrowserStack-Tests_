from pytest_bdd import given, when, then, scenarios
from selenium.webdriver.common.by import By

# initilize a driver from seleniumbase in instance
# driver = Driver()

# Scenarios
scenarios('./features/CheckLogin.feature')

# constants
DEMO_QA_LOGIN_PAGE = "https://demoqa.com/login"


@given("i open login page")
def step_impl(driver):
    driver.get(DEMO_QA_LOGIN_PAGE)
    print("STEP 1: demoqa login page opened\n")


@when("i enter username value")
def step_impl(driver):
    driver.find_element(By.ID("userName")).send_keys("ch_demoqa")
    print("STEP 2: username value entered\n")


@when("i enter password value")
def step_impl(driver):
    driver.find_element(By.ID("password")).send_keys("Admin1234!")
    print("STEP 3: password value entered\n")


@when("i click in login button")
def step_impl(driver):
    driver.find_element(By.ID("login"))
    print("STEP 4: login button clicked\n")


@then("navigate to profile page and success login")
def step_impl(driver):
    current_username = driver.find_element(By.ID("userName-value"))
    assert current_username.text == "ch_demoqa"
    print("login and navigate to profile page passed")
