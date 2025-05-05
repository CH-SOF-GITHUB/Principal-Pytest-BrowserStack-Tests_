"""
🔁 7. Search a new phrase from the results page
Description: Perform a new search using the search box while on the results page.

Purpose: Tests in-page search functionality. Ensures:

Previous results are cleared

New results show up correctly
"""
import pytest

from pages.home import DuckDuckGoHomePage
from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage


@pytest.mark.parametrize('expected_phrase, expected_new_search', [('python', 'pycharm'), ('panda', 'selenium')])
def test_basic_duckduckgo_search_new_phrase_from_results_page(driver_initialization, expected_phrase,
                                                              expected_new_search):
    # Initialize the pages object model classes in instance
    home_page = DuckDuckGoHomePage(driver=driver_initialization)
    search_page = DuckDuckGoSearchPage(driver=driver_initialization)
    result_page = DuckDuckGoResultPage(driver=driver_initialization)

    # declare an url constante
    url = "https://www.duckduckgo.com/"

    # declare an expected_phrase to enter as input data in my test
    # expected_phrase = "python"

    try:
        # Given the DuckDuckGo home page is displayed
        home_page.load(url=url)

        # When the user searches for "panda"
        search_page.search_by_button(Text=expected_phrase)

        # Then the search result title contains "panda"
        result_page.get_title(to_search=expected_phrase)

        # And the search result query is "panda"
        actual_input_search_value = result_page.search_input_value()
        assert actual_input_search_value == expected_phrase

        # And the search result links pertain to "panda"
        actual_titles = result_page.get_title_links()
        print("\n****** Titles Links:  ******")
        for i, title in enumerate(actual_titles):
            assert expected_phrase.lower() in title.text.lower()
            print(f"result title link: {i + 1} = {title.text}")

        # And Search a new phrase from the results page
        # expected_new_search = "panda"
        result_page.enter_new_search_from_results_page(new_search=expected_new_search)

        driver_initialization.set_page_load_timeout(7)

        print(f"\n******New search url: {driver_initialization.current_url} *******")

        new_actual_titles = result_page.get_title_links()

        # Previous results are cleared
        assert expected_phrase.lower() not in [title.text.lower() for title in new_actual_titles]
        print("Previous results are cleared")

        # New results show up correctly
        print("\n****** New Search Titles Links:  ******")
        for i, title in enumerate(new_actual_titles):
            assert expected_new_search.lower() in title.text.lower()
            print(f"result title link: {i + 1} = {title.text}")

    except Exception as e:
        raise Exception("Incomplete Test")
