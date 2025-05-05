"""
These tests cover DuckDuckGo searches.
TC009: do a video search
"""
import pytest
from selenium.common import NoSuchElementException

from pages.home import DuckDuckGoHomePage
from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage
from tests.conftest import driverConfig
from utils.hooks import take_screenshot


class VideoMode:
    YOUTUBE = "YouTube"
    VIMEO = "Vimeo"


# , 'selenium', 'web driver'
@pytest.mark.parametrize('expected_phrase', ['python'])
def test_basic_duckduckgo_do_a_video_search(driverConfig, expected_phrase):
    # Initialize the pages object model classes in instance
    home_page = DuckDuckGoHomePage(driver=driverConfig)
    search_page = DuckDuckGoSearchPage(driver=driverConfig)
    result_page = DuckDuckGoResultPage(driver=driverConfig)

    # declare an url constante
    url = "https://www.duckduckgo.com/"

    # declare an expected_phrase to enter as input data in my test

    try:
        # Given the DuckDuckGo home page is displayed
        home_page.load(url=url)

        # When the user searches for "panda"
        search_page.search(Text=expected_phrase)

        # Then the search result title contains "panda"
        result_page.get_title(to_search=expected_phrase)

        # And the search result query is "panda"
        actual_search_value = result_page.search_input_value()
        assert actual_search_value == expected_phrase

        # Switch to videos tab
        result_page.click_videos_link()

        # vidéos are loaded and appear correctly
        i = 1
        all_videos = []
        while i < 5:
            try:
                element_video = result_page.all_videos_of_search_for_description(i)
                all_videos.append(element_video)
                i += 1
            except NoSuchElementException as e:
                print(str(e))

        print(f"\n********** Total videos loaded: {len(all_videos)} **********")

        # display all descriptions of videos
        print("\n********** videos with descriptions **********")
        i = 0
        while i < len(all_videos):
            print(f"Video {i + 1} with title {all_videos[i].text}")
            i = i + 1

        # Link to the correct sources (e.g., YouTube, Vimeo)
        k = 1
        videos_to_be_clicked = []
        while k < 5:
            try:
                video_to_be_clicked = result_page.all_videos_of_search_for_click(k)
                videos_to_be_clicked.append(video_to_be_clicked)
                k = k + 1
            except NoSuchElementException as e:
                print(str(e))

        print(f"\nlength of videos_to_be_clicked: {len(videos_to_be_clicked)}")

        print("\n********** Link to the correct sources **********")
        for i, video in enumerate(videos_to_be_clicked):
            try:
                if VideoMode.YOUTUBE in video.text:
                    print(f"video {i + 1} is a {VideoMode.YOUTUBE} video")
                    video.click()
                    print(f"video {i + 1} is clicked")
                    print(f"current url for video {i + 1}: {driverConfig.current_url}")
                elif VideoMode.VIMEO in video.text:
                    print(f"video {i + 1} is a {VideoMode.VIMEO} video")
                    video.click()
                    print(f"video {i + 1} is clicked")
                else:
                    print(f"Video {i + 1} source is unknown or not specified as YouTube/Vimeo.")
            except Exception as e:
                print(str(e))

        # take a screenshots for the final success results after verification
        take_screenshot(driverConfig, "success_do_a_video_search___" + expected_phrase + ".png")
    except Exception as e:
        take_screenshot(driverConfig, "bug_do_a_video_search___" + expected_phrase + ".png")
        raise Exception("Incomplete Test")
