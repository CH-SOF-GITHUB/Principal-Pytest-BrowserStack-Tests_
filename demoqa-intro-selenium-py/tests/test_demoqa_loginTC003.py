"""
These tests cover Demoqa login with valid credentials
"""
import os
import time

import dotenv
import pytest
from dotenv import load_dotenv

from pages.dashboard import DashboardPageDemoQA
from pages.login import LoginPageDemoQA


def setStatus(status, request):
    test_name = request.node.name
    print(f"\nTest {test_name} ----------- status: {status}")


load_dotenv(dotenv.find_dotenv())

DEMO_QA_PATH_SCREENSHOT = os.environ.get("DEMOQA_PATH_SCREENSHOT")


# test with valid credentials
@pytest.mark.parametrize("expected_username, expected_pwd", [("ch_demoqa", "Admin1234!"),
                                                             ("BenSalehdemoqa", "Admin1234!"),
                                                             ("TarekDemoQA", "Azerty1234!"),
                                                             ("ali.tawfiki.01", "demoQA12345*")])
def test_basic_demoqa_login_valid_credentials(driver_initialize, expected_username, expected_pwd, request):
    driver, browser = driver_initialize
    # Given the DemoQA login page is displayed
    login_page = LoginPageDemoQA(driver)
    # Given the DemoQA dashboard page is displayed
    dashboard_page = DashboardPageDemoQA(driver)
    try:
        print("\nTest Case STEPS: ")
        # Enter valid username
        login_page.enter_username(expected_username)

        # Enter valid password
        login_page.enter_password(expected_pwd)

        # scroll to bottom y  200
        driver.execute_script("window.scrollTo(0, window.scrollY + 200)")

        # Click in login button
        login_page.click_login_button()

        # attente 5s to load page response
        time.sleep(5)

        # assert url of page change to dashboard url
        dashboard_page.change_current_url_to_dashboard(new_url="https://demoqa.com/profile")

        # assert the new value of username
        actual_username_value = dashboard_page.dashboard_username()
        assert expected_username == actual_username_value, "the 2 values of username in dashboard are different !"

        # return a message for the final results
        setStatus("Passed", request=request)

        # take a screenshot for the final results
        # driver.save_screenshot(
        #     "C:\\Users\\chaker\\PycharmProjects\\pytest-browserstack\\demoqa-intro-selenium-py\\resultsImages\\success_" + browser + "_demoqa_login__valid_credentials__" + expected_username + expected_pwd + ".png")

    except Exception as e:
        # driver.save_screenshot(
        #    "C:\\Users\\chaker\\PycharmProjects\\pytest-browserstack\\demoqa-intro-selenium-py\\resultsImages\\bug_" + browser + "_demoqa_login__valid_credentials__" + expected_username + expected_pwd + ".png")
        raise Exception(f"Incomplete Test : {str(e)}")
