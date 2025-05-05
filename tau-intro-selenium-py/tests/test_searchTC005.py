"""
expand "More Results" at the bottom of the result page
"""
import threading
import time

import pytest

from pages.home import DuckDuckGoHomePage
from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage

"""
Un test paramétré est une méthode de test qui permet d’exécuter 
la même fonction de test plusieurs fois avec différentes données d'entrée (appelées paramètres).
"""


@pytest.mark.parametrize("expected_phrase", ["DuckDuckGo"])
def test_basic_duckduckgo_search_more_results(driverConfig, expected_phrase):
    # initialize the object page classes
    home_page = DuckDuckGoHomePage(driver=driverConfig)
    search_page = DuckDuckGoSearchPage(driver=driverConfig)
    result_page = DuckDuckGoResultPage(driver=driverConfig)

    # url of web-site
    url = "https://www.duckduckgo.com"

    print('\n')
    print(threading.current_thread().name, ' | ', threading.current_thread().ident, 'Starting')
    try:
        # Given the DuckDuckGo home page is displayed
        home_page.load(url=url)

        # When the user searches for "panda"
        search_page.search(expected_phrase)

        # Then the search result title contains "panda"
        result_page.get_title(expected_phrase)

        # And the search result query is "panda"
        actual_result = result_page.search_input_value()
        assert actual_result == expected_phrase

        # Recherches associées
        actualTitles = result_page.get_title_links()
        for i, actualTitle in enumerate(actualTitles):
            assert expected_phrase.lower() in actualTitle.text.lower()
            print(f"Actual result Title {i + 1}: {actualTitle.text}")

        initial_links = result_page.get_links_site()

        # click in more results button
        result_page.click_more_results()
        print("\nClicked 'More Results' button.")

        # Ajouter une attente explicite pour s'assurer que le DOM est mis à jour
        result_page.wait_for_new_results(len(initial_links))

        # Now retrieve the new results
        new_links = result_page.get_links_site()

        # Compare results
        if set(new_links) == set(initial_links):
            print("No new results found after clicking 'More Results'.\n")
        else:
            print(f"{len(new_links) - len(initial_links)} new results successfully loaded.\n")

        # Debugging new output
        if len(initial_links) > 0 and len(new_links) > 0:
            print("\nInitial Links Loaded:")
            for k, link in enumerate(initial_links):
                print(f"Initial Link {k + 1}: {link.text}")

            print("\nNew Links Loaded starting from last index of initial links:")
            start_index = len(initial_links)
            for idx, link in enumerate(new_links[start_index:], start=start_index + 1):
                print(f"New Link {idx}: {link.text}")

        # verify result final
        print('expand "More Results" at the bottom of the result page passed ok')

    except Exception as e:
        raise Exception(f"Incomplete Test: {e}")

    print(threading.current_thread().name, ' | ', threading.current_thread().ident, 'Ending')

    t = threading.Thread(name='test_basic_duckduckgo_search_more_results_service',target=test_basic_duckduckgo_search_more_results)
    t.start()
