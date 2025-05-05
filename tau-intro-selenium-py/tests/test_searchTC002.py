import pytest

from pages.home import DuckDuckGoHomePage
from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage
from utils.hooks import take_screenshot

"""
search for different phrases
"""


# running tests in parallel
@pytest.mark.parametrize('expected_phrase', ['panda', 'python', 'polar'])
def test_basic_duckduckgo_search_multiple(driverConfig, expected_phrase):
    # initialize the page object classes
    home_page = DuckDuckGoHomePage(driver=driverConfig)
    search_page = DuckDuckGoSearchPage(driver=driverConfig)
    result_page = DuckDuckGoResultPage(driver=driverConfig)

    # declare the url constante
    url = "https://duckduckgo.com/"
    # expected_phrase = "panda"
    try:
        # Given the DuckDuckGo home page is displayed
        home_page.load(url=url)

        # When the user searches for "panda"
        search_page.search(expected_phrase)

        # Then the search result title contains "panda"
        result_page.get_title(expected_phrase)

        # And the search result query is "panda"
        actual_result = result_page.search_input_value()
        assert expected_phrase == actual_result

        # And the search result links pertain to "panda"
        actual_links = result_page.get_title_links()
        for link in actual_links:
            assert expected_phrase.lower() in link.text.lower()

        # verify results
        print("search multiple for -" + expected_phrase + "- passed ok")

        # take a screenshot for the result
        take_screenshot(driverConfig, 'search-multiple-' + expected_phrase + '.png')

    except Exception as e:
        take_screenshot(driverConfig, 'bug-search-multiple-' + expected_phrase + '.png')
        raise Exception("Incomplete Test")
