from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.home import HomePageDemoQa
from selenium.webdriver.support import expected_conditions as EC

class BookPageDemoQA(HomePageDemoQa):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def get_books(self, i):
        wait = WebDriverWait(self.driver, 10)
        book_element = wait.until(EC.visibility_of_element_located((By.XPATH,f"//*[@id='app']/div/div/div/div[2]/div[2]/div[2]/div[1]/div[2]/div[{i}]/div/div[2]/div")))
        return book_element