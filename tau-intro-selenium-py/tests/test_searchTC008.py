"""
On DuckDuckGo, after performing a regular search, you can switch to the Images tab to see image results related to your search query.

Goals of the Image Search Test
Perform a search for a specific term (e.g., "cats")
Switch to the Images tab
Verify that images are displayed
Optionally, verify that the images are relevant

"""

import pytest
from selenium.common import NoSuchElementException

from pages.home import DuckDuckGoHomePage
from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage
from utils.hooks import take_screenshot

"""
These tests cover DuckDuckGo searches.
"""


@pytest.mark.parametrize('b', ['chrome'])
def test_basic_duckduckgo_image_search(browser, b):
    # Initialize the pages object model classes in instance
    home_page = DuckDuckGoHomePage(driver=browser)
    search_page = DuckDuckGoSearchPage(driver=browser)
    result_page = DuckDuckGoResultPage(driver=browser)

    # declare an url constante
    url = "https://www.duckduckgo.com/"

    # declare an expected_phrase to enter as input data in my test
    expected_phrase = "python"
    try:
        # Given the DuckDuckGo home page is displayed
        home_page.load(url=url)

        # When the user searches for "panda"
        search_page.search(expected_phrase)

        # Switch to the Images tab
        result_page.click_images_link(10, 'linkText', 'Images')
        # Verify that images are displayed
        print("current url of images: " + browser.current_url)
        # Optionally, verify that the images are relevant
        allImages = set()
        for i in range(1, 5):
            try:
                image_element = result_page.all_images_of_search(i)
                allImages.add(image_element)
            except NoSuchElementException as e:
                print(e.msg)
                continue

        print(f"\n******* {len(allImages)} images with description: ")
        for i, image in enumerate(allImages):
            print(f'Image {i + 1} _ description: ' + image.get_attribute('alt'))

        take_screenshot(browser, "do-an-image-search--" + expected_phrase + ".png")
    except Exception as e:
        take_screenshot(browser, "bug-do-an-image-search--" + expected_phrase + ".png")
        raise Exception("Incomplete Test")
