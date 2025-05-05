from os import environ

import pytest
import urllib3
from selenium import webdriver
from selenium.common import WebDriverException
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.safari.options import Options as SafariOptions

urllib3.disable_warnings()


# conftest driver control web driver ----------------------------------------------------------------------------------
@pytest.fixture()
def driver():
    # Initialize the web driver in instance
    b = webdriver.Chrome()

    # Make its calls wait up to 10s for elements to appear
    b.implicitly_wait(10)

    # Return the WebDriver instance for the setup
    yield b

    # Quit the WebDriver instance for the cleanup
    b.quit()


# ---------------------------------------------------------------------------------------------------------------------
def browsers():
    return ["chrome", "firefox", "edge"]


def getBrowser(request):
    return request.param


@pytest.fixture(params=browsers())
def driver_selenium_server(request):
    # Assuming you are running a local Selenium Grid or Standalone server
    global driver
    global options
    global browser
    options = None
    driver = None
    if request.param == "chrome":
        options = ChromeOptions()
        options.page_load_strategy = 'none'
        browser = request.param
        #print(f"\n********  browser executed : {request.param}  ********")
    elif request.param == "firefox":
        options = FirefoxOptions()
        options.page_load_strategy = 'none'
        browser = request.param
        #print(f"\n********  browser executed : {request.param}  ********")
    elif request.param == "edge":
        options = EdgeOptions()
        options.page_load_strategy = 'none'
        browser = request.param
        #print(f"\n********  browser executed : {request.param}  ********")
    else:
        print("provide a valid browser name from this list chrome/firefox")
    driver = webdriver.Remote(
        command_executor='http://192.168.1.100:4444/wd/hub',
        options=options
    )
    # return the web driver instance
    yield driver, browser
    # set implicit wait to 10s
    driver.implicitly_wait(10)
    # quit the web driver for cleanup
    driver.quit()


# ---------------------------------------------------------------------------------------------------------------------
emusim_browsers = [
    {
        "deviceName": "iPhone X Simulator",
        "browserName": "Safari",
        "deviceOrientation": "portrait",
        "platformVersion": "13.4",
        "platformName": "iOS"
    }, {
        "deviceName": "iPhone 11 Simulator",
        "browserName": "Safari",
        "deviceOrientation": "portrait",
        "platformVersion": "13.4",
        "platformName": "iOS"
    }, {
        "deviceName": "Google Pixel 3 XL GoogleAPI Emulator",
        "browserName": "Chrome",
        "deviceOrientation": "portrait",
        "platformVersion": "10.0",
        "platformName": "Android"
    }, {
        "deviceName": "Samsung Galaxy S9 WQHD GoogleAPI Emulator",
        "browserName": "Chrome",
        "deviceOrientation": "portrait",
        "platformVersion": "9.0",
        "platformName": "Android"
    }]

desktop_browsers = [
    {
        "platformName": "Windows 11",
        "browserName": "chrome",
        "platformVersion": "latest",
        "sauce:options": {}
    },
    {
        "platformName": "Windows 11",
        "browserName": "firefox",
        "platformVersion": "latest",
        "sauce:options": {}
    }]


# ------------------------- Selenium Grid hub build Sauce Labs ---------------------------------------------------------
def pytest_addoption(parser):
    parser.addoption("--dc", action="store", default='us', help="Set Sauce Labs Data Center (US or EU)")


@pytest.fixture
def data_center(request):
    return request.config.getoption('--dc')


# ------------------------------------------------------------------------------------------------------
@pytest.fixture(params=desktop_browsers)
def desktop_web_driver(request, data_center):
    global username
    global access_key
    test_name = request.node.name
    build_tag = environ.get('BUILD_TAG', "Sauce-Best-Practices-Python-Desktop-Web")

    username = 'oauth-bensaid.chaker-c8a05'
    access_key = 'ddb05cca-dc95-44ff-a099-3645e43af455'

    if data_center and data_center.lower() == 'eu':
        selenium_endpoint = "https://{}:{}@ondemand.eu-central-1.saucelabs.com/wd/hub".format(username, access_key)
    else:
        selenium_endpoint = "https://{}:{}@ondemand.us-west-1.saucelabs.com/wd/hub".format(username, access_key)

    caps = dict()
    caps.update(request.param)
    caps['sauce:options'].update({'build': build_tag})
    caps['sauce:options'].update({'name': test_name})

    browser = webdriver.Remote(
        command_executor=selenium_endpoint,
        options=webdriver.ChromeOptions(),
        keep_alive=True
    )

    # This is specifically for SauceLabs plugin.
    # In case test fails after selenium session creation having this here will help track it down.
    if browser is not None:
        print("SauceOnDemandSessionID={} job-name={}".format(browser.session_id, test_name))
    else:
        raise WebDriverException("Never created!")

    yield browser

    # Teardown starts here
    # report results
    # use the test result to send the pass/fail status to Sauce Labs
    sauce_result = "failed" if request.node.rep_call.failed else "passed"
    browser.execute_script("sauce:job-result={}".format(sauce_result))
    browser.quit()


# Add the pytest_runtest_makereport hook to capture test results
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # set a report attribute for each phase of a call, which can be "setup", "call", "teardown"
    setattr(item, "rep_" + rep.when, rep)


# ------------------------- Selenium Grid build Lambdatest -------------------------------------------------------------
@pytest.fixture(params=["chrome", "firefox", "safari"], scope='function')
def driver_grid_build(request):
    # Get the username and accesskey
    username = "bchaker28"
    accesskey = "LT_z3NSTniUUMFpDiAk87KaVuhA3mv5NQsKHK12MwZ8lLLuqlS"

    # Get the Grid URL for executing tests on LambdaTest
    selenium_grid_url = f"https://{username}:{accesskey}@hub.lambdatest.com/wd/hub"

    test_name = request.node.name

    lt_options = {
        "platform": "Windows 11",
        "version": "latest",
        "name": test_name,
        "build": "build v_06 connecting to selenium server or selenium grid Test Case: register",
        "video": True,
        "visual": True,
        "network": True,
        "console": True,
        # To enable detailed Selenium logs to debug issues of your application
        "verboseWebDriverLogging": True,
        # Terminal Logs are enabled for this test
        "terminal": True,
        # Device Logs are enabled for this test
        "devicelog": True,
        # To view performance metrics
        "performance": True,
        # Unlock accessibility features for your account by contacting our support team
        "accessibility": True,
        "smartUI.project": "Pytest DemoQA Suite Tests TC00X",
        "selenium_version": "4.0.0",
        "browser_version": "latest"
    }

    # Desired capabilities for Selenium Grid or BrowserStack
    if request.param == "chrome":
        chrome_options = ChromeOptions()
        chrome_options.set_capability("LT:Options", lt_options)
        # Create Remote WebDriver
        driver = webdriver.Remote(command_executor=selenium_grid_url, options=chrome_options)
    elif request.param == "firefox":
        firefox_options = FirefoxOptions()
        firefox_options.set_capability("LT:Options", lt_options)
        # Create Remote WebDriver
        driver = webdriver.Remote(command_executor=selenium_grid_url, options=firefox_options)
    elif request.param == "safari":
        safari_options = SafariOptions()
        safari_options.set_capability("LT:Options", lt_options)
        driver = webdriver.Remote(command_executor=selenium_grid_url, options=safari_options)
    else:
        raise Exception("Web driver not supported")
    # return the remote web driver instance for the setup
    yield driver

    # quit the web driver for the cleanup
    driver.quit()
