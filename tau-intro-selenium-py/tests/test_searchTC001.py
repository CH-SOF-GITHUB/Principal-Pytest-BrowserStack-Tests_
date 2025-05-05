"""
These tests cover DuckDuckGo searches.
"""
import threading

from pages.home import DuckDuckGoHomePage
from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage
from utils.hooks import take_screenshot

"""
search for single phrase
"""
"""
Performance gain and Threads
First why I've been always using threads for speeding up my selenium code:

On I/O bound tasks my experience with selenium shows that there's minimal or no difference between 
using a pool of Processes (Process) or Threads (Threads). 
Here also reach similar conclusions about Python threads vs processes on I/O bound tasks.
We also know that processes use their own memory space. That means more memory consumption. 
Also processes are a little slower to be spawned than threads.
"""

def test_basic_duckduckgo_search(browser):
    try:
        print('\n')
        print(threading.current_thread().name, ' | ', threading.current_thread().ident, 'Starting')

        # Initilize page objets classes
        homePage = DuckDuckGoHomePage(driver=browser)
        searchPage = DuckDuckGoSearchPage(driver=browser)
        resultPage = DuckDuckGoResultPage(driver=browser)

        url = "https://www.duckduckgo.com/"

        expected_phrase = "panda"
        # Given the DuckDuckGo home page is displayed
        homePage.load(url=url)

        # When the user searches for "panda"
        searchPage.search(expected_phrase)

        # Then the search result title contains "panda"
        resultPage.get_title(expected_phrase)

        # And the search result query is "panda"
        assert expected_phrase == resultPage.search_input_value()

        # And the search result links pertain to "panda"
        actual_results = resultPage.get_title_links()
        for actual_result in actual_results:
            assert expected_phrase.lower() in actual_result.text.lower()

        # verify results
        print("single search for -" + expected_phrase + "- passed ok")

        print(threading.current_thread().name, ' | ', threading.current_thread().ident, 'Ending')

        # Determining the Current Thread
        w = threading.Thread(name='test_basic_duckduckgo_search', target=test_basic_duckduckgo_search)
        w.start()

        # take a screenshot for the result
        take_screenshot(browser, 'search-single-' + expected_phrase + '.png')

    except Exception as e:
        raise Exception("Incomplete Test")
