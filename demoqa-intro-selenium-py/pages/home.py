class HomePageDemoQa:

    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        print(f"\nDemoQa page opened with url: {url}")
