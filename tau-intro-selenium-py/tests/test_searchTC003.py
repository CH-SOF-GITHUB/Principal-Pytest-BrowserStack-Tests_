"""
search by clicking the button instead of typing RETURN
"""
import pytest

from pages.home import DuckDuckGoHomePage
from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage
from utils.hooks import take_screenshot

"""
search by clicking the button instead of typing RETURN

with using,  Cross-Browser Testing is the process of verifying that 
a website or web application works correctly across different web browsers, browser versions, 
and platforms.
"""


@pytest.mark.parametrize('b', ['chrome', 'firefox'])
def test_basic_duckduckgo_search_clicking_button(browser, b):
    # initialize the object page classes
    home_page = DuckDuckGoHomePage(driver=browser)
    search_page = DuckDuckGoSearchPage(driver=browser)
    result_page = DuckDuckGoResultPage(driver=browser)

    # url of web-site
    url = "https://www.duckduckgo.com"

    # expected_phrase to search
    expected_phrase = "python"
    try:
        # Given the DuckDuckGo home page is displayed
        home_page.load(url)

        # When the user searches for "panda"
        search_page.search_by_button(expected_phrase)

        # Then the search result title contains "panda"
        result_page.get_title(expected_phrase)

        # And the search result query is "panda"
        actual_phrase = result_page.search_input_value()
        assert expected_phrase == actual_phrase

        # And the search result links pertain to "panda"
        actual_links = result_page.get_title_links()
        for link in actual_links:
            assert expected_phrase.lower() in link.text.lower()

        # verify results
        print("search by clicking the button instead of typing RETURN for -" + expected_phrase + 'in-browser' + b + "- passed ok")

        # take a screenshot for the final results
        take_screenshot(browser, 'search-clicking-button-' + expected_phrase + 'in-browser' + b + '.png')
    except Exception as e:
        raise Exception("Incomplete Test")
