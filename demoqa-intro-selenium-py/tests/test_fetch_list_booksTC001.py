import os
import time

import dotenv
import pytest

from pages.book import BookPageDemoQA
from pages.dashboard import DashboardPageDemoQA
from pages.login import LoginPageDemoQA

dotenv.load_dotenv(dotenv.find_dotenv())


@pytest.mark.bug("C41", "Minor bug", run=True)
def test_fetch_list__books(driver_initialize):
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
        print("\nTest Case STEPS: ")
        # Enter valid username
        login_page.enter_username("ch_demoqa")

        # Enter valid password
        login_page.enter_password("Admin1234!")

        # scroll to bottom y  200
        driver.execute_script("window.scrollTo(0, window.scrollY + 200)")

        # Click in login button
        login_page.click_login_button()

        # declare the expected titles of books that added in profile
        expected_books_titles = ['Git Pocket Guide', 'Learning JavaScript Design Patterns',
                                 'Designing Evolvable Web APIs with ASP.NET', 'Speaking JavaScript',
                                 'Programming JavaScript Applications']

        # fetch the books in the table
        books_demoqa = []
        i = 1
        while i < 6:
            book = book_page.get_books(i)
            books_demoqa.append(book)
            i = i + 1

        # wait for 3 seconds before exist the execution
        time.sleep(3)

        # loop through the 2 arrays of books to assert with the expected title of book
        print("\n------------- Loop through the 2 arrays of books to assert with expected title of book -------------")
        for acutal_book, expected_book in zip(books_demoqa, expected_books_titles):
            assert acutal_book.text == expected_book
            print(f"actual book: '{acutal_book.text}' == expected book: '{expected_book}'")
        # k = 0
        # for book in books_demoqa:
        #    assert book.text == expected_books_titles[k]
        #    print(book.text + f" = expected book {k + 1} : " + expected_books_titles[k])
        #    k = k + 1

        # take a screenshot for books
        # driver.save_screenshot(f"{PATH_SCREENSHOT}//success_get_books.png")
    except Exception as e:
        raise f"Incompleted Test: {str(e)}"