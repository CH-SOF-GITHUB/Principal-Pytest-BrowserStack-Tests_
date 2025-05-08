# Fixtures
import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    b = webdriver.Chrome()
    b.implicitly_wait(10)
    # yield driver for the setup
    yield b
    # quit driver for the cleanup
    b.quit()
