import logging
import os
import time

import dotenv
from pytest_bdd import given, when, then, scenarios

from pages.book import BookPageDemoQA
from pages.login import LoginPageDemoQA

dotenv.load_dotenv(dotenv.find_dotenv())

logger = logging.getLogger(__name__)
# scenarios
SCENARIO_PATH = os.environ.get("SCENARIOS_PATH")
scenarios(f"{SCENARIO_PATH}//NavigatePages.feature")

# constants
DEMO_QA_LOGIN_PAGE = "https://demoqa.com/login"


@given("i open login page")
def step_impl(driver):
    # create an instance from login page
    LoginPageDemoQA(driver)
    print("\nSTEP 1: demoqa login page opened\n")


@when("i navigate to profile")
def step_impl(driver):
    login_page = LoginPageDemoQA(driver)
    login_page.enter_username("ch_demoqa")
    login_page.enter_password("Admin1234!")
    # scroll to Y 200
    driver.execute_script("window.scrollTo(0, scrollY + 200)")
    login_page.click_login_button()


@when("i navigate to book store")
def step_impl(driver):
    time.sleep(3)
    last_scroll_height = driver.execute_script("return document.body.scrollHeight")
    SCROLL_PAUSE_TIME = 0.5
    while driver.current_url == "https://demoqa.com/profile":
        # scroll down to bottom
        logger.info("last scroll height:  " + str(last_scroll_height))
        driver.execute_script("window.scrollBy(0,925)", "")
        time.sleep(SCROLL_PAUSE_TIME)
        new_scroll_height = driver.execute_script("return document.body.scrollHeight")
        logger.info("new scroll height:   " + str(new_scroll_height))
        if new_scroll_height == last_scroll_height:
            break
        last_scroll_height = new_scroll_height


@then("i logout with success")
def step_impl(driver):
    time.sleep(1)
    bookstore_page = BookPageDemoQA(driver)
    bookstore_page.go_book_store()
    time.sleep(1)
    bookstore_page.click_logout()
    time.sleep(1)
    assert driver.current_url == "https://demoqa.com/login"
    print(f"\nRESULT: i logout and switch with success to '{driver.current_url}'")