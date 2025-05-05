from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators.locators import DuckDuckGoResultLocators


class LocatorMode:
    XPATH = "xpath"
    CSS_SELECTOR = "cssSelector"
    NAME = "name"
    ID = "id"
    TAG_NAME = "tagName"
    CLASS_NAME = "className"
    LINK_TEXT = "linkText"
    PARTIAL_LINK_TEXT = "partialLinkText"


class DuckDuckGoResultPage:
    # constructor of class
    def __init__(self, driver):
        self.driver = driver

    # Methods of class
    def get_title_links(self):
        wait = WebDriverWait(self.driver, 10)
        links = wait.until(EC.visibility_of_all_elements_located(DuckDuckGoResultLocators.result_titles_locator))
        # return table of results
        return links

    def get_links_site(self):
        wait = WebDriverWait(self.driver, 10)
        linksSite = wait.until(
            EC.visibility_of_all_elements_located(DuckDuckGoResultLocators.result_links_site_locator))
        return linksSite

    def search_input_value(self):
        wait = WebDriverWait(self.driver, 10)
        input_search = wait.until(
            EC.visibility_of_element_located(DuckDuckGoResultLocators.result_search_field_locator))
        value = input_search.get_attribute('value')
        return value

    def get_title(self, to_search):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.title_contains(to_search))

    def click_more_results(self):
        wait = WebDriverWait(self.driver, 10)
        btnMoreResults = wait.until(EC.element_to_be_clickable(DuckDuckGoResultLocators.more_results_locator))
        btnMoreResults.click()

    def wait_for_new_results(self, previous_count, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            lambda driver: len(
                driver.find_elements(*DuckDuckGoResultLocators.result_links_site_locator)) > previous_count
        )

    def enter_new_search_from_results_page(self, new_search):
        wait = WebDriverWait(self.driver, 10)
        result_search_input = wait.until(
            EC.visibility_of_element_located(DuckDuckGoResultLocators.result_search_input_adv_locator))
        result_search_input.clear()
        result_search_input.send_keys(new_search + Keys.RETURN)

    def click_images_link(self, waitTime, locatorMode, Locator):
        element = None
        # locatorMode = 'linkText'
        if locatorMode == LocatorMode.LINK_TEXT:
            element = WebDriverWait(self.driver, waitTime).until(
                EC.presence_of_element_located((By.LINK_TEXT, Locator)))
        element.click()
        print("search images link clicked !")

    def all_images_of_search(self, i):
        wait = WebDriverWait(self.driver, 10)
        xpath = f'//*[@id="react-layout"]/div/div[2]/div/div[2]/section/ol/li[1]/ol/li[{i}]/figure/div/img'
        images = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
        return images

    # click in videos link method
    def click_videos_link(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located(DuckDuckGoResultLocators.videos_link))
        element.click()
        print("search vidéos link clicked !")

    # return off all vidéos of search
    def all_videos_of_search_for_description(self, iterator):
        wait = WebDriverWait(self.driver, 10)
        video = wait.until(EC.visibility_of_element_located(
            (By.XPATH, f'//*[@id="react-layout"]/div/div[2]/div/div[2]/ol/li[{iterator}]/a/article/div[2]/h2')))
        return video

    # return of all vidéos of search to be clicked
    def all_videos_of_search_for_click(self, iterator):
        wait = WebDriverWait(self.driver, 10)
        video = wait.until(EC.visibility_of_element_located(
            (By.XPATH, f'//*[@id="react-layout"]/div/div[2]/div/div[2]/ol/li[{iterator}]/a')))
        return video

    # ----------------------- change regions for results methods ---------------------------------- #
    def change_region_for_results(self, region_to_change):
        wait = WebDriverWait(self.driver, 10)
        # 1 click in region_filter drop down
        element = wait.until(EC.visibility_of_element_located(DuckDuckGoResultLocators.region_filter_label_locator))
        element.click()
        print("\nregion filter drop down clicked !")
        # 2 select the region to change for results of search
        regions = wait.until(EC.visibility_of_all_elements_located(DuckDuckGoResultLocators.region_name_locator))
        all_regions = []
        for region in regions:
            all_regions.append(region)
        # print(all_regions)
        for region in all_regions:
            if region.text == region_to_change:
                region.click()
                print(f"\nregion changed to : " + region_to_change)
                break


"""
# region in regions:
        #    print("regions all implemented !")
        #    if region.text == region_to_change:
        #        region.click()
        #        print(f"region changed to " + region_to_change)
"""
