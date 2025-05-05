"""
These tests cover Demoqa login.
"""
import time

import pytest

from pages.login import LoginPageDemoQA


@pytest.mark.parametrize("expected_username, expected_password", [("ch_demoqa", "Admin1234!")])
def test_basic_demoqa_login(driver_selenium_server, expected_username, expected_password):
    # Initialize the page objects in instance
    login_page = LoginPageDemoQA(driver_selenium_server)

    browser_turned_on = driver_selenium_server.current_window_handle
    print("browser turned on: " + browser_turned_on)
    try:
        # 1. enter username
        login_page.enter_username(expected_username)

        # 2. enter password
        login_page.enter_password(expected_password)

        driver_selenium_server.execute_script("window.scrollTo(0, window.scrollY + 200)")

        # 3. click login button
        login_page.click_login_button()

        timeout = time.time() + 10
        i = 0
        while True:
            if i == 5 or time.time() > timeout:
                print("\ncurrent url : " + driver_selenium_server.current_url)
                break
            i = i - 1

        print("\nattendre login page")

        # print a message for the final results
        print("\nTest demoqa login passed")

        # take a screenshot for the final results
        driver_selenium_server.save_screenshot(
            "C:\\Users\\chaker\\PycharmProjects\\pytest-browserstack\\demoqa-intro-selenium-py\\resultsImages\\success_demoqa_login.png")
    except Exception as e:
        driver_selenium_server.save_screenshot(
            "C:\\Users\\chaker\\PycharmProjects\\pytest-browserstack\\demoqa-intro-selenium-py\\resultsImages\\bug_demoqa_login.png")
        raise Exception(f"Incomplete Test : {str(e)}")
