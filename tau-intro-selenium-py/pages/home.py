class DuckDuckGoHomePage:

    # constructor of class
    def __init__(self, driver):
        self.driver = driver

    # Methods of class
    def load(self, url):
        self.driver.get(url)
