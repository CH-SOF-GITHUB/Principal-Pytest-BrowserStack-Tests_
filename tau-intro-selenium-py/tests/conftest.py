import json
import os

import pytest
from selenium import webdriver


@pytest.fixture(scope='session')
def config():
    # Read the file
    with open(
            'C:\\Users\\chaker\\PycharmProjects\\pytest-browserstack\\tau-intro-selenium-py\\utils\\config.json',
            'r') as config_file:
        config = json.load(config_file)

    # Assert values are acceptable
    assert config['browser'] in ['Chrome', 'Firefox', 'Headless Chrome']
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0

    # Return a config so that can be used
    return config


@pytest.fixture
def driverConfig(config):
    # Initialize the WebDriver instance
    if config['browser'] == 'Chrome':
        b = webdriver.Chrome()
    elif config['browser'] == 'Firefox':
        b = webdriver.Firefox()
    elif config['browser'] == 'Headless Chrome':
        opts = webdriver.ChromeOptions()
        opts.add_argument('headless')
        b = webdriver.Chrome(options=opts)
    else:
        raise Exception(f'Unsupported browser : {config["browser"]}')
    # Make its calls wait up to 10 seconds for elements to appear
    b.implicitly_wait(10)

    # Return the WebDriver instance for the setup
    yield b

    # Quit the WebDriver instance for the cleanup
    b.quit()


@pytest.fixture()
def browser(b):
    # Initialize the WebDriver instance
    if b is None:
        d = webdriver.Chrome()
    elif b == 'chrome':
        d = webdriver.Chrome()
    elif b == 'firefox':
        d = webdriver.Firefox()
    elif b == 'edge':
        d = webdriver.Edge()
    elif b == 'headless chrome':
        opts = webdriver.ChromeOptions()
        opts.add_argument('headless')
        d = webdriver.Chrome(options=opts)
    else:
        raise Exception(f'Unsupported browser : {b}')
    # Make its calls wait up to 10 seconds for elements to appear
    d.implicitly_wait(10)

    # Return the WebDriver instance for the setup
    yield d

    # Quit the WebDriver instance for the cleanup
    d.quit()


"""
# use selenium grid to scal out parallel testing
@pytest.fixture(scope='function')
def driver():
    # parallize_test_accross_combinations
    username = os.getenv("LT_USERNAME")  # Replace the username
    access_key = os.getenv("LT_ACCESS_KEY")  # Replace the access key

    # paste your capibility options below

    options = ChromeOptions()
    options.browser_version = "latest"
    options.platform_name = "Windows 11"
    lt_options = {}
    lt_options["username"] = username
    lt_options["accessKey"] = access_key
    lt_options["video"] = True
    # lt_options["resolution"] = "1920x1080"
    lt_options["network"] = True
    lt_options["visual"] = True
    lt_options["network"] = True
    lt_options["build"] = "tau-intro-selenium-py build v01"
    # lt_options["project"] = "unit_testing"
    lt_options["smartUI.project"] = "test"
    lt_options["name"] = "tau-intro-selenium-py DuckDuckGo search Tests"
    lt_options["w3c"] = True
    lt_options["plugin"] = "python-python"
    options.set_capability("LT:Options", lt_options)

    # Initialize the ChromeDriver instance
    b = webdriver.Remote(
        command_executor="http://{}:{}@hub.lambdatest.com/wd/hub".format(
            username, access_key
        ),
        options=options,
    )

    # Return the WebDriver instance for the setup
    yield b

    # Quit the WebDriver instance for the cleanup
    b.quit()
"""

"""
cross browser test with selenium grid: Initialize Driver for selenium Grid 
on LambdaTest: param.request:
"""


@pytest.fixture(params=["chrome", "firefox", "internet explorer"])
def driver_initialization(request):
    browser = None
    test_name = request.node.name
    build = os.environ.get('BUILD', "Sample PYTEST Build")
    tunnel_id = os.getenv('TUNNEL', False)
    username = os.getenv('LT_USERNAME', None)
    access_key = os.getenv('LT_ACCESS_KEY', None)

    selenium_endpoint = f"http://{username}:{access_key}@hub.lambdatest.com/wd/hub"
    option = {
        "platform": "Windows 11",
        "version": "latest",
        "name": test_name,
        "build": "build v_05 Selenium Grid pytest tau-intro-selenium-py TC-change_region",
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
        "smartUI.project": "Pytest-Tau-Intro-Selenium-Py Suite Tests TC00X",
        "selenium_version": "4.0.0",
        "browser_version": "latest"
    }
    if request.param == "chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.set_capability("LT:Options", option)
        browser = webdriver.Remote(
            command_executor=selenium_endpoint,
            options=chrome_options
        )
    elif request.param == "firefox":
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.set_capability("LT:Options", option)
        browser = webdriver.Remote(
            command_executor=selenium_endpoint,
            options=firefox_options
        )
    elif request.param == "safari":
        safari_options = webdriver.SafariOptions()
        safari_options.set_capability("LT:Options", option)
        browser = webdriver.Remote(
            command_executor=selenium_endpoint,
            options=safari_options
        )
    elif request.param == "internet explorer":
        ie_options = webdriver.IeOptions()
        ie_options.set_capability("LT:Options", option)
        browser = webdriver.Remote(
            command_executor=selenium_endpoint,
            options=ie_options
        )
    elif request.param == "edge":
        edge_options = webdriver.EdgeOptions()
        edge_options.set_capability("LT:Options", option)
        browser = webdriver.Remote(
            command_executor=selenium_endpoint,
            options=edge_options
        )
    else:
        print("request of browser not supported")
    # Return web driver to use
    yield browser
    # Take a screenshot at the end of the test
    browser.quit()


def initialize_driver(request):
    pass
