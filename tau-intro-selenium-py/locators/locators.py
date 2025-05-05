from selenium.webdriver.common.by import By


class DuckDuckGoSearchLocators(object):
    search_input_locator = (By.ID, 'searchbox_input')
    search_button_locator = (By.XPATH, '//*[@id="searchbox_homepage"]/div/div[1]/div/button[2]')
    # searchbox_searchButton__LxebD
    # check method visibility
    searchbox_suggestions_locator = 'searchbox_suggestions__5vqa7'
    searchbox_suggestions_option_locator = 'searchbox_suggestion__2TYYJ'


class DuckDuckGoResultLocators(object):
    result_search_field_locator = (By.ID, 'search_form_input')
    result_titles_locator = (By.CSS_SELECTOR, 'a.result__a')
    more_results_locator = (By.ID, 'more-results')
    result_links_site_locator = (By.XPATH, '//a[@data-testid="result-title-a"]')
    # locators to search from results page
    result_search_input_adv_locator = (By.CLASS_NAME, 'search__input--adv')
    search_form_input_clear_locator = (By.ID, 'search_form_input_clear')
    # locator of images search link
    images_link = (By.LINK_TEXT, 'Images')

    # locator for images search
    result_img_locator = (
        By.XPATH, '//*[@id="react-layout"]/div/div[2]/div/div[2]/section/ol/li[1]/ol/li[1]/figure/div/img')

    # locator of videos search link By.XPATH, //*[@id="react-duckbar"]/div/div/section/nav/ul[1]/li[3]/a
    videos_link = (By.XPATH, '//*[@id="react-duckbar"]/div/div/section/nav/ul[1]/li[3]/a')

    # shared locator for vidéos search
    results_video_locator = (By.CLASS_NAME, 'xrWcR15SIZQFwwZBfYi3')
    # ----------------------------------------------------------------------------------------------------
    region_filter_label_locator = (By.XPATH, '//*[@id="react-layout"]/div/div/div/div[1]/nav/div[2]/div/div[1]/span[1]/div/div/a')
    region_name_locator = (By.CLASS_NAME, 'fdosLIuRgrWo7SyeqSUb')
    # ----------------------------------------------------------------------------------------------------


class SettingsPageLocators(object):
    # sidebar menu locator in home page
    sidemenu_button_locator = (
    By.XPATH, '//*[@id="__next"]/div/main/article/div[1]/div[1]/div[2]/div/header/div/section[3]/nav/ul/li/button')

    # settings link locator
    settings_link = (
    By.XPATH, '/html/body/div[1]/div/main/article/div[1]/div[1]/div[2]/div/header/div[2]/div/section[1]/ul/li[3]/p/a')
    # settings_link = (By.LINK_TEXT, "Paramètres")
    # settings_link_ = (By.XPATH, '//*[@id="__next"]/div/main/article/div[1]/div[1]/div[2]/div/header/div[2]/div/section[1]/ul/li[3]/p/a')

    # langue title locator
    langue_title_locator = (By.XPATH, "//*[@id='content_internal']/div[1]/div[1]/div[2]/form/div[2]/p[1]")
    # Langue d'affichage select locator
    langue_select_locator = (By.ID, "setting_kad")

    # safe search level title locator
    safe_search_level_title_locator = (By.XPATH, "//*[@id='content_internal']/div[1]/div[1]/div[2]/form/div[4]/p[1]")
    # safe mode search level select locator
    safe_mode_search_level_select_locator = (By.ID, "setting_kp")

    # General link locator
    general_link_locator = (By.XPATH, '//*[@id="content_internal"]/div[1]/div[1]/div[1]/div/a[1]')

    # Apparence Mode link locator
    apparence_mode_link_locator = (By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[1]/div[1]/div/a[2]")

    # click button save and exist locator
    button_save_and_exist_locator = (By.CLASS_NAME, 'js-set-exit')
