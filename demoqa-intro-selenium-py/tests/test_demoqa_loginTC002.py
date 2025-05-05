"""
These tests cover Demoqa login.
"""
import time

import pytest

from pages.dashboard import DashboardPageDemoQA
from pages.login import LoginPageDemoQA


@pytest.mark.parametrize("expected_username, expected_password", [("ch_demoqa", "Admin1234!")])
def test_basic_demoqa_login(driver_selenium_server, expected_username, expected_password, driver=None):
    # Initialize wb driver
    driver, browser = driver_selenium_server
    # Initialize the page objects in instance
    login_page = LoginPageDemoQA(driver)
    dashboard_page = DashboardPageDemoQA(driver)

    current_window_handle_turned_on = driver.current_window_handle
    print("\nbrowser turned on: " + current_window_handle_turned_on)
    try:
        # 1. enter username
        login_page.enter_username(expected_username)

        # 2. enter password
        login_page.enter_password(expected_password)

        driver.execute_script("window.scrollTo(0, window.scrollY + 200)")

        # 3. click login button
        login_page.click_login_button()

        timeout = time.time() + 10
        i = 0
        while True:
            if i == 6 or time.time() > timeout:
                print("\ncurrent url : " + driver.current_url)
                break
            i = i - 1

        # assert the expected value of username in dashboard
        actual_username = dashboard_page.dashboard_username()
        print("\nDashboard username: " + actual_username)
        assert actual_username == expected_username

        # print a message for the final results
        print("\nTest demoqa login passed")

        # take a screenshot for the final results
        driver.save_screenshot(
            "C:\\Users\\chaker\\PycharmProjects\\pytest-browserstack\\demoqa-intro-selenium-py\\resultsImages\\success_" + browser + "_demoqa_login.png")
    except Exception as e:
        driver.save_screenshot(
            "C:\\Users\\chaker\\PycharmProjects\\pytest-browserstack\\demoqa-intro-selenium-py\\resultsImages\\bug_" + browser + "_demoqa_login.png")
        raise Exception(f"Incomplete Test : {str(e)}")
