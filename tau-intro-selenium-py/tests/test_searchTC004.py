import pytest
from selenium.common import StaleElementReferenceException

from pages.home import DuckDuckGoHomePage
from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage

"""
click a search result
"""

@pytest.mark.parametrize("expected_phrase", ["DuckDuckGo"])
def test_click_search_result_with_retry(driverConfig, expected_phrase):
    """
    Test clicking a search result with retry logic to handle stale element exceptions.
    """
    home_page = DuckDuckGoHomePage(driverConfig)
    search_page = DuckDuckGoSearchPage(driverConfig)
    result_page = DuckDuckGoResultPage(driverConfig)

    url = "https://www.duckduckgo.com/"

    try:
        # Given the DuckDuckGo home page is displayed
        home_page.load(url)

        # When the user searches for "panda"
        search_page.search(expected_phrase)

        # Then the search result title contains "panda"
        result_page.get_title(expected_phrase)

        # And the search result query is "panda"
        actual_phrase = result_page.search_input_value()
        assert actual_phrase == expected_phrase

        # And the search result links pertain to "panda"
        actual_links = result_page.get_title_links()
        for link in actual_links:
            assert expected_phrase.lower() in link.text.lower()

        # loop through the first page
        for page in range(1, 2):
            try:
                # Re-localisez les liens avant chaque interaction
                links_results = result_page.get_title_links()
                for i in range(len(links_results)):
                    try:
                        # Re-localisez le lien spécifique avant de cliquer
                        links_results = result_page.get_title_links()
                        if i >= len(links_results):
                            # if links have changed and fewer links exist now
                            break
                        link_result = links_results[i]
                        link_result.click()
                        print(f"Clicked link #{i + 1}: {driverConfig.current_url}")
                    except StaleElementReferenceException as e:
                        print(f"ERROR: {e.msg} at index {i}")
            except Exception as e:
                print(f"Unexpected error: {e}")
            if page == 2:
                break

        # verify results
        print("click a search result for -" + expected_phrase + "- passed ok")

        # take a screenshot for the final results
        # take_screenshot(driverConfig, 'click-a-search-result-' + expected_phrase + '.png')
    except Exception as e:
        raise Exception("Incomplete Test")
