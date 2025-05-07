"""
These tests cover demoqa login with invalid credentials.
"""
import os

import dotenv
import pytest
from dotenv import load_dotenv

from pages.login import LoginPageDemoQA
from tests.conftest import driver_initialize


def setStatus(status, request):
    test_name = request.node.name
    print(f"\nTest {test_name} ----------- status: {status}")


load_dotenv(dotenv.find_dotenv())

DEMO_QA_PATH_SCREENSHOT = os.environ.get("DEMOQA_PATH_SCREENSHOT")


# test with invalid credentials
@pytest.mark.parametrize("expected_username, expected_pwd, expected_errorMsg", [
    # TC1: username invalid and password valid
    ("chdemoqa", "Admin1234!", "Invalid username or password!"),
    # TC2: username valid and password invalid
    ("BenSalehdemoqa", "", ""),
    # TC3: username invalid and password invalid
    # ("TarekDemo", "Aze1234!", "Invalid username or password!"),
    # TC4: username vide and password vide
    ("", "", "")
])
def test_basic_demoqa_login_invalid_credentials(driver_initialize, expected_username, expected_pwd, expected_errorMsg,
                                                request):
    # Initialize the WebDriver and the browser in instance
    driver, browser = driver_initialize

    # Initialize the object pages in instance
    login_page = LoginPageDemoQA(driver)

    try:
        print("\nTest case STEPS:  ")
        # enter username
        login_page.enter_username(expected_username)

        # enter password
        login_page.enter_password(expected_pwd)

        # scroll down with 200 y
        driver.execute_script("window.scrollTo(0, scrollY + 200)")

        # click the login button
        login_page.click_login_button()

        if expected_username != "" and expected_pwd != "":
            # return the error message ofr username and password
            errorMessage = login_page.error_message()
            if errorMessage.is_displayed():
                print("\nlogin error message is displayed")
                # verify the expected error messages
                actualErrorMessage = login_page.get_error_message()
                assert actualErrorMessage == expected_errorMsg
                print(f"\nerror message is : {actualErrorMessage}")
        elif expected_username != "" or expected_pwd != "":
            inputErrorMessages = login_page.inputs_error_message()
            assert len(inputErrorMessages) == 1
        else:
            inputErrorMessages = login_page.inputs_error_message()
            if len(inputErrorMessages) > 0:
                assert inputErrorMessages[0].get_attribute("value") == expected_username
                assert inputErrorMessages[1].get_attribute("value") == expected_pwd

        setStatus(status="Passed", request=request)

        # take a screenshot for the final results
        # driver.save_screenshot(
        #    f"{DEMO_QA_PATH_SCREENSHOT}\\success_" + browser + "_Test_demoqa_login__fails__" + expected_username + expected_pwd + ".png")
    except Exception as e:
        # driver.save_screenshot(
        #    f"{DEMO_QA_PATH_SCREENSHOT}\\bug_" + browser + "_Test_demoqa_login__fails__" + expected_username + expected_pwd + ".png")
        raise Exception(f"Incomplete Test : {str(e)}")
