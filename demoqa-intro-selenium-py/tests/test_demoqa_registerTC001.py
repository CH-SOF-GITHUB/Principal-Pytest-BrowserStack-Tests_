"""
These tests cover DemoQA register.
"""
import time

import pytest


from pages.home import HomePageDemoQa
from pages.register import RegisterPageDemoQA

"""
register demoqa
"""


@pytest.mark.parametrize('expected_firstname, expected_lastname, expected_username, expected_password',
                         [('Chaker', 'ben said', 'ch_demoqa', 'Admin1234!')])
def test_basic_demoqa_register(driver_selenium_server, expected_firstname, expected_lastname, expected_username,
                               expected_password):
    home_page = HomePageDemoQa(driver_selenium_server)
    register_page = RegisterPageDemoQA(driver_selenium_server)

    try:
        # Given the Demoqa register page is displayed
        # enter the firstname "chaker"
        register_page.enter_firstname(expected_firstname)

        # enter the lastname "ben said"
        register_page.enter_lastname(expected_lastname)

        # enter the username "ch_demoqa"
        register_page.enter_username(expected_username)

        # enter the password "Admin1234"
        register_page.enter_password(expected_password)
        driver_selenium_server.execute_script("window.scrollTo(0, window.scrollY + 200)")
        # click in recaptcha_checkbox_border
        register_page.click_recaptcha_checkbox()
        time.sleep(2)

        # click in the register button
        register_page.click_register_button()

        # verify the register is passed
        assert driver_selenium_server.current_url == "https://demoqa.com/login"

        # print a message for the final results
        print("Test demoqa register passed")

        # take an image for the final results
        driver_selenium_server.save_screenshot(
            "C:\\Users\\chaker\\PycharmProjects\\pytest-browserstack\\demoqa-intro-selenium-py\\resultsImages\\success_demoqa_register.png")
    except Exception as e:
        driver_selenium_server.save_screenshot(
            "C:\\Users\\chaker\\PycharmProjects\\pytest-browserstack\\demoqa-intro-selenium-py\\resultsImages\\bug_demoqa_register.png")
        raise Exception(f"Incomplete Test : {str(e)}")
