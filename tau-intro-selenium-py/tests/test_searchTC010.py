"""
These tests cover DuckDuckGo searches.
TC010: change settings
"""
import time

import pytest

from pages.home import DuckDuckGoHomePage
from pages.search import DuckDuckGoSearchPage
from pages.settings import DuckDuckGoSettingsPage

"""
Tests data: 
    English = "English (United States)"
            Moderate_en = "Moderate"
            Strict_en = "Strict"
            Off_en = "Off"
    Francais = "Français (France)"
            Moderate_fr = "Modéré"
            Strict_fr = "Strict"
            Off_fr = "Désactivé"
    Deutsch = "Deutsch (Deutschland)"
            Moderate_Gr = "Moderat"
            Strict_Gr = "Streng"
            Off_Gr = "Aus"

expected_langue_option = "English (United States)"
expected_mode_search = "Off"

Default_en = "default"
Basic_en = "basic"
Contrast_en = "contrast"
Dark_en = "dark"
Gray_en = "gray"
Terminal_en = "terminal"
"""


@pytest.mark.parametrize("expected_langue_option, expected_mode_search, expected_apparence_mode",
                         [("English (United States)", "Strict", "Basic"),
                          ("English (United States)", "Moderate", "Dark"),
                          ("English (United States)", "Off", "Contrast")
                          ])
def test_basic_duckduckgo_change_settings(driver_initialization, expected_langue_option, expected_mode_search,
                                          expected_apparence_mode):
    # Initialize the pages object model classes in instance
    home_page = DuckDuckGoHomePage(driver=driver_initialization)
    search_page = DuckDuckGoSearchPage(driver=driver_initialization)
    settings_page = DuckDuckGoSettingsPage(driver=driver_initialization)

    # declare an url constante
    url = "https://duckduckgo.com/"
    try:
        # Given the DuckDuckGo home page is displayed
        home_page.load(url=url)

        # click into sidemenu button
        settings_page.click_sidemenu_button()

        # click into settings link
        settings_page.click_settings_menu_link()

        # set page load timeout 7 SECONDS
        driver_initialization.set_page_load_timeout(7)

        # verify the navigate to settings page
        # actual_currentUrl = driverConfig.current_url
        # expected_currentUrl = "https://duckduckgo.com/settings"
        # assert actual_currentUrl == expected_currentUrl

        # change options: Default language
        settings_page.turn_langue_options(optionLangue=expected_langue_option)
        time.sleep(2)
        print(f"******* default language changed to '{expected_langue_option}' *******")
        expected_langue_label = settings_page.get_langue_title()
        print("Display Langue Title is : " + expected_langue_label)

        # change options: Safe search level (Strict, Moderate, Off)
        settings_page.turn_safe_search_level(mode_search=expected_mode_search)
        time.sleep(2)
        print(f"******* safe search level changed to '{expected_mode_search}' *******")
        expected_safe_search_title = settings_page.get_safe_search_title()
        print("safe search level Title is : " + expected_safe_search_title)

        # change options: Appearance (Light/Dark Mode)
        # click in Apparence mode link
        settings_page.click_apparence_link()
        time.sleep(2)
        assert "appearance" in driver_initialization.current_url
        settings_page.turn_apparence_mode(apparence_mode=expected_apparence_mode)

        # time 3 s
        time.sleep(3)

        # save/apply options.
        settings_page.click_button_save_and_exist()

        # control navigate to back
        settings_page.click_settings_menu_link()

        # time 5 s to load response of page
        time.sleep(5)

        # verify the settings page works and options are saved/applied.
        assert expected_langue_option in driver_initialization.page_source
        assert expected_mode_search in driver_initialization.page_source
        settings_page.click_apparence_link()
        # time 2 s to verify final results
        time.sleep(2)
        assert expected_apparence_mode in driver_initialization.page_source
        print('Test change settings ok\n')
    except Exception as e:
        raise Exception("Incomplete Test : {}".format(str(e)))
