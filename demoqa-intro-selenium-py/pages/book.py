from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BookPageDemoQA:
    def __init__(self, driver):
        self.driver = driver

    def get_books(self, i):
        wait = WebDriverWait(self.driver, 10)
        book_element = wait.until(EC.visibility_of_element_located((By.XPATH,f"//*[@id='app']/div/div/div/div[2]/div[2]/div[2]/div[1]/div[2]/div[{i}]/div/div[2]/div")))
        return book_element

    def go_book_store(self):
        wait = WebDriverWait(self.driver, 10)
        button = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="gotoStore"]')))
        button.click()
        print("\nSTEP 4: book store button clicked")

    def click_logout(self):
        wait = WebDriverWait(self.driver, 10)
        button = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="submit"]')))
        button.click()
        print("\nSTEP 5: logout button clicked")
