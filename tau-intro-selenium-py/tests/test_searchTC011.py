"""
These tests cover DuckDuckGo searches.
TC011: change region
"""
import json

import pytest

from pages.home import DuckDuckGoHomePage
from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage
from utils.hooks import take_screenshot

"""
run the same tests with multiple sets of input data, eliminating the need for redundant test code.

With parameterized testing, you can easily cover different scenarios and edge cases and provide better test coverage.
"""


def openConfig():
    with open('C:\\Users\\chaker\\PycharmProjects\\pytest-browserstack\\tau-intro-selenium-py\\utils\\config.json',
              'r') as file:
        config = json.load(file)
        return config


# define multiple sets of arguments and fixtures at the function test
@pytest.mark.parametrize('expected_phrase', ['python', 'selenium', 'parametrize'])
def test_basic_duckduckgo_search_change_region(driverConfig, expected_phrase, config):
    # Initialize the pages object model classes in instance
    home_page = DuckDuckGoHomePage(driver=driverConfig)
    search_page = DuckDuckGoSearchPage(driver=driverConfig)
    result_page = DuckDuckGoResultPage(driver=driverConfig)

    # declare an url constante
    url = "https://duckduckgo.com/"

    # expected_phrase to be search
    try:
        # Given the DuckDuckGo home page is displayed
        home_page.load(url=url)

        # When the user searches for "panda"
        search_page.search(Text=expected_phrase)

        # Then the search result title contains "panda"
        result_page.get_title(to_search=expected_phrase)

        # And the search result query is "panda"
        actual_input_search_phrase = result_page.search_input_value()
        assert actual_input_search_phrase == expected_phrase

        # verify the titles of search after change region
        print("\n************ Titles of links search before change of region ************")
        try:
            actual_titles_search_before_change = result_page.get_title_links()
            for i, title in enumerate(actual_titles_search_before_change):
                print(f"title found {i + 1} : {title.text}")
                assert expected_phrase.lower() in title.text.lower()
        except Exception as e:
            print(str(e))
        # change the region for results
        result_page.change_region_for_results("États-Unis")

        # verify the change of region
        print("\nAfter change region, regional results and preferences are applied correctly !")

        # verify the titles of search after change region
        print("\n************ Titles of links search after change region ************")
        actual_titles_search_after_change = result_page.get_title_links()
        for i, title in enumerate(actual_titles_search_after_change):
            print(f"title found {i + 1} : {title.text}")
            assert expected_phrase.lower() in title.text.lower()
        config = openConfig()
        take_screenshot(driverConfig,
                        "success__change__region_to_search__" + config["browser"] + "__" + expected_phrase + ".png")
    except Exception as e:
        take_screenshot(driverConfig,
                        "bug__change__region_to_search__" + config["browser"] + "__" + expected_phrase + ".png")
        raise Exception("Incomplete Test: {}".format(str(e)))
