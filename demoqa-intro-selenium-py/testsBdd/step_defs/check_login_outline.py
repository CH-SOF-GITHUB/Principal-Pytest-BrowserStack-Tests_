import os
import time

import dotenv
import pytest
from pytest_bdd import given, when, then, scenarios
from pytest_bdd.parsers import parse
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

dotenv.load_dotenv(dotenv.find_dotenv())

# scenarios
SCENARIO_PATH = os.environ.get("SCENARIOS_PATH")
scenarios(f"{SCENARIO_PATH}//CheckLoginOutline.feature")
# constants
DEMO_QA_LOGIN_PAGE = "https://demoqa.com/login"


def find(driver):
    wait = WebDriverWait(driver, 10)
    return wait.until(EC.visibility_of_element_located((By.ID, "userName-value")))


@given("i open login page")
def step_impl(driver):
    driver.get(DEMO_QA_LOGIN_PAGE)
    driver.implicitly_wait(10)
    driver.maximize_window()
    print("\nSTEP 1: demoqa login page opened\n")


@when(parse("i enter username value {username}"))
@when("i enter username value <username>")
def step_impl(driver, username):
    username_field = driver.find_element(By.ID, "userName")
    username_field.send_keys(username)
    print("STEP 2: username value entered\n")


@when(parse("i enter password value {password}"))
@when("i enter password value <password>")
def step_impl(driver, password):
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys(password)
    print("STEP 3: password value entered\n")


@when("i click in login button")
def step_impl(driver):
    # scroll in to login button element
    driver.execute_script("window.scrollTo(0, scrollY + 200)")
    login_button = driver.find_element(By.XPATH, "//*[@id='login']")
    login_button.click()
    print("STEP 4: login button clicked\n")


@then(parse('i verify the {status} login with {username}'))
@then("i verify the <status> login with <username>")
def step_impl(driver, status, username):
    # wait for 5 s for load page response
    time.sleep(5)
    try:
        # driver.current_url == "https://demoqa.com/profile" and username in driver.page_source and
        if find(driver).text == username:
            print(f"RESULT: Status Login {status}")
        else:
            pytest.fail(f"RESULT: Status Login {status}")
    except Exception as e:
        pytest.fail(f"Error is: {str(e)}")
