import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class MyTestCase(unittest.TestCase):
    def setUp(self):
        options = Options()
        # {"browserName":"chrome","platformName":"Windows 11"}
        self.driver = webdriver.Remote(
            command_executor='http://192.168.1.100:4444/wd/hub',
            options=options
        )

    def test_google(self):
        self.driver.get("https://www.google.com")
        self.assertIn("Google", self.driver.title)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
