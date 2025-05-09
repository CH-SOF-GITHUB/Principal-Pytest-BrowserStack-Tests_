# Fixtures
import pytest
from selenium import webdriver


def browsers():
    return ["chrome", "firefox", "edge"]


@pytest.fixture(params=["chrome"], autouse=True)
def driver(request):
    b = None
    test_name = request.node.name
    print(f"\n------------------- TEST : '{test_name}' is running -------------------")
    if request.param == "chrome":
        b = webdriver.Chrome()
    elif request.param == "firefox":
        b = webdriver.Firefox()
    elif request.param == "edge":
        b = webdriver.Edge()
    else:
        print("web driver not supported")
    # implicit wait for web element to 10 s
    b.implicitly_wait(10)
    # yield driver for the setup
    yield b
    # quit driver for the cleanup
    b.quit()
