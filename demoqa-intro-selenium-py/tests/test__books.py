import os
import time

import dotenv

from pages.book import BookPageDemoQA
from pages.dashboard import DashboardPageDemoQA
from pages.login import LoginPageDemoQA

dotenv.load_dotenv(dotenv.find_dotenv())


def test_books(driver_initialize):
    # Initialize the WebDriver and the browser in instance
    driver, browser = driver_initialize
    # Given the DemoQA login page is displayed
    login_page = LoginPageDemoQA(driver)
    # Given the DemoQA dashboard page is displayed
    dashboard_page = DashboardPageDemoQA(driver)
    # Given the DemoQA book page is displayed
    book_page = BookPageDemoQA(driver)

    # Path of screenshot
    PATH_SCREENSHOT = os.environ.get("DEMOQA_PATH_SCREENSHOT")
    try:
        # Enter valid username
        login_page.enter_username("ch_demoqa")

        # Enter valid password
        login_page.enter_password("Admin1234!")

        # scroll to bottom y  200
        driver.execute_script("window.scrollTo(0, window.scrollY + 200)")

        # Click in login button
        login_page.click_login_button()

        # fetch the books in the table
        books_demoqa = []
        i = 1
        while i < 6:
            book = book_page.get_books(i)
            books_demoqa.append(book)
            i = i + 1

        # wait for 3 seconds before exist the execution
        time.sleep(3)

        k = 0
        while k < len(books_demoqa):
            print(f"\nbook {k + 1} : {books_demoqa[k].text} ")
            k = k + 1

        # take a screenshot for books
        driver.save_screenshot(f"{PATH_SCREENSHOT}//success_get_books.png")
    except Exception as e:
        raise f"Incompleted Test: {str(e)}"
