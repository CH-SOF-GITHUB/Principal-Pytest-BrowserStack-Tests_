"""
These tests cover DuckDuckGo searches.
verify auto-complete suggestions pertain to the search text
search by selecting an auto-complete suggestion
"""

import pytest

from locators.locators import DuckDuckGoSearchLocators
from pages.home import DuckDuckGoHomePage
from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage
from utils.hooks import take_screenshot


@pytest.mark.parametrize("partial_phrase", ["pychar"])
@pytest.mark.parametrize("expected_search", ["pycharm", "pycharm free"])
def test_basic_duckduckgo_search_verify_auto_complete_suggestions(driverConfig, partial_phrase, expected_search):
    # Initialize the object pages of classes
    home_page = DuckDuckGoHomePage(driverConfig)
    search_page = DuckDuckGoSearchPage(driverConfig)
    result_page = DuckDuckGoResultPage(driverConfig)

    # url constante
    url = 'https://www.duckduckgo.com/'

    # ==> data-driven testing is going

    # expected_search = "pycharm"
    try:
        # Given the DuckDuckGo home page is displayed
        home_page.load(url=url)

        # When the user searches for "panda"
        search_page.enter_input_search(partial_phrase)

        # wait for drop-down suggestions visible: (self, waitTime, locatorMode, Locator)
        search_page.wait_for_auto_complete_suggestions_visibility(10, "className",
                                                                  DuckDuckGoSearchLocators.searchbox_suggestions_locator)

        print("drop-down auto complete suggestions is visible now !")

        # list of suggestions if visible : (self, waitTime, locatorMode, Locator, Text)
        suggestions_options = search_page.list_of_suggestions(10, "className",
                                                              DuckDuckGoSearchLocators.searchbox_suggestions_option_locator)

        print('list of suggestions generated')

        # verify auto-complete suggestions pertain to the search text
        found = False
        for option in suggestions_options:
            option_text = option.text.strip()
            if expected_search == option_text:
                # search by selecting an auto-complete suggestion
                option.click()
                print(f"verified uto-complete suggestion option and clicked {option_text}")
                found = True
                break

        if not found:
            raise Exception(f"Verified uto-complete suggestion option not found for {expected_search}")

        if found:
            print(driverConfig.current_url)
            # Then the search result title contains "panda"
            result_page.get_title(expected_search)

            # And the search result query is "panda"
            actual_search = result_page.search_input_value()
            assert actual_search == expected_search

            # And the search result links pertain to "panda"
            titles = result_page.get_title_links()
            if len(titles) > 0:
                for title in titles:
                    assert expected_search.lower() in title.text.lower()

            # And the search result titles pertain to "expected_search"
            initial_links = result_page.get_links_site()
            if len(initial_links) > 0:
                print("\nInitial Links Loaded:")
                for i, link in enumerate(initial_links):
                    print(f"initial link {i} : {link.text}")

                # take a screenshot for the final result
                take_screenshot(driverConfig,
                                "auto-complete-suggestions--for--" + partial_phrase + "--pertain-to--" + expected_search + ".png")

    except Exception as e:
        # take a screenshot for the final bug
        take_screenshot(driverConfig,
                        "bug-auto-complete-suggestions--for--" + partial_phrase + "--pertain-to--" + expected_search + ".png")
        raise Exception("Incomplete Test")
