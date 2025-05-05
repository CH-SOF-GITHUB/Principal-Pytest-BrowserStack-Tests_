from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from locators.locators import SettingsPageLocators


class ModeSearch:
    Moderate_fr = "Modéré"
    Strict_fr = "Strict"
    Off_fr = "Désactivé"
    Moderate_en = "Moderate"
    Strict_en = "Strict"
    Off_en = "Off"
    Moderate_Gr = "Moderat"
    Strict_Gr = "Streng"
    Off_Gr = "Aus"
    Moderate_tr = "Orta"  # -1
    Strict_tr = "Katı"
    Off_tr = "Kapalı"


class LangueOptions:
    Arabic = "العربية (السعودية)"  # value=ar_SA
    English = "English (United States)"  # value=en_US
    Persian = "فارسی"  # value=fa_IR
    Francais = "Français (France)"  # value=fr_FR
    Turkey = "Türkçe (Türkiye)"  # value=tr_TR
    Deutsch = "Deutsch (Deutschland)"  # value=de_DE


class AppearanceMode:
    Default_en = "Default"
    Basic_en = "Basic"
    Contrast_en = "Contrast"
    Dark_en = "Dark"
    Gray_en = "Gray"
    Terminal_en = "Terminal"
    Default_fr = "Défaut"
    Basic_fr = "Basique"
    Contrast_fr = "Contraste"
    Dark_fr = "Sombre"
    Gray_fr = "Gris"
    Terminal_fr = "Terminal"


class DuckDuckGoSettingsPage:
    def __init__(self, driver):
        self.driver = driver

    # -------------------------------------------------------------------------------------------------------
    def click_sidemenu_button(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable(SettingsPageLocators.sidemenu_button_locator))
        element.click()
        print("\nsidemenu button clicked !")

    # -------------------------------------------------------------------------------------------------------
    def click_settings_menu_link(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(SettingsPageLocators.settings_link))
        element.click()

    # -------------------------------------------------------------------------------------------------------
    # get title of safe search level
    def get_safe_search_title(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(SettingsPageLocators.safe_search_level_title_locator))
        return element.text

    def turn_safe_search_level(self, mode_search):
        wait = WebDriverWait(self.driver, 10)
        try:
            safe_modes_search_level = wait.until(
                EC.visibility_of_element_located(SettingsPageLocators.safe_mode_search_level_select_locator))
            select = Select(safe_modes_search_level)
            # click safe search level
            if ModeSearch.Moderate_fr == mode_search:
                select.select_by_value("-1")
            elif ModeSearch.Strict_fr == mode_search:
                select.select_by_value("1")
            elif ModeSearch.Off_fr == mode_search:
                select.select_by_value("-2")
            elif ModeSearch.Moderate_en == mode_search:
                select.select_by_value("-1")
            elif ModeSearch.Strict_en == mode_search:
                select.select_by_value("1")
            elif ModeSearch.Off_en == mode_search:
                select.select_by_value("-2")
            elif ModeSearch.Moderate_Gr == mode_search:
                select.select_by_value("-1")
            elif ModeSearch.Strict_Gr == mode_search:
                select.select_by_value("1")
            elif ModeSearch.Off_Gr == mode_search:
                select.select_by_value("-2")
            elif ModeSearch.Moderate_tr == mode_search:
                select.select_by_value("-1")
            elif ModeSearch.Strict_tr == mode_search:
                select.select_by_value("1")
            elif ModeSearch.Off_tr == mode_search:
                select.select_by_value("-2")
            else:
                print("select mode search not supported")
        except Exception as e:
            print(str(e))

    # ----------------------------------------------------------------------------------------------------------------
    def get_langue_title(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(SettingsPageLocators.langue_title_locator))
        return element.text

    def turn_langue_options(self, optionLangue):
        wait = WebDriverWait(self.driver, 10)
        try:
            langue_options = wait.until(EC.visibility_of_element_located(SettingsPageLocators.langue_select_locator))
            select = Select(langue_options)
            # click langue option chose
            if LangueOptions.Arabic == optionLangue:
                select.select_by_value("ar_SA")
            elif LangueOptions.English == optionLangue:
                select.select_by_value("en_US")
            elif LangueOptions.Persian == optionLangue:
                select.select_by_value("fa_IR")
            elif LangueOptions.Francais == optionLangue:
                select.select_by_value("fr_FR")
            elif LangueOptions.Turkey == optionLangue:
                select.select_by_value("tr_TR")
            elif LangueOptions.Deutsch == optionLangue:
                select.select_by_value("de_DE")
            else:
                print("langue option not supported")
        except Exception as e:
            print(str(e))

    # -----------------------------------------------------------------------------------------------------------
    def click_general_link(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(SettingsPageLocators.general_link_locator))
        element.click()

    # -----------------------------------------------------------------------------------------------------------
    def click_apparence_link(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(SettingsPageLocators.apparence_mode_link_locator))
        element.click()
        print("Appearance mode link clicked !")

    def turn_apparence_mode(self, apparence_mode):
        element = None
        wait = WebDriverWait(self.driver, 10)
        if AppearanceMode.Default_en == apparence_mode:
            element = wait.until(EC.visibility_of_element_located((By.XPATH, "//label[@data-theme-id='-1']")))
        elif AppearanceMode.Basic_en == apparence_mode:
            element = wait.until(EC.visibility_of_element_located((By.XPATH, "//label[@data-theme-id='b']")))
        elif AppearanceMode.Contrast_en == apparence_mode:
            element = wait.until(EC.visibility_of_element_located((By.XPATH, "//label[@data-theme-id='c']")))
        elif AppearanceMode.Dark_en == apparence_mode:
            element = wait.until(EC.visibility_of_element_located((By.XPATH, "//label[@data-theme-id='d']")))
        elif AppearanceMode.Gray_en == apparence_mode:
            element = wait.until(EC.visibility_of_element_located((By.XPATH, "//label[@data-theme-id='g']")))
        elif AppearanceMode.Terminal_en == apparence_mode:
            element = wait.until(EC.visibility_of_element_located((By.XPATH, "//label[@data-theme-id='t']")))
        elif AppearanceMode.Default_fr == apparence_mode:
            element = wait.until(EC.visibility_of_element_located((By.XPATH, "//label[@data-theme-id='-1']")))
        elif AppearanceMode.Basic_fr == apparence_mode:
            element = wait.until(EC.visibility_of_element_located((By.XPATH, "//label[@data-theme-id='b']")))
        elif AppearanceMode.Contrast_fr == apparence_mode:
            element = wait.until(EC.visibility_of_element_located((By.XPATH, "//label[@data-theme-id='c']")))
        elif AppearanceMode.Dark_fr == apparence_mode:
            element = wait.until(EC.visibility_of_element_located((By.XPATH, "//label[@data-theme-id='d']")))
        elif AppearanceMode.Gray_fr == apparence_mode:
            element = wait.until(EC.visibility_of_element_located((By.XPATH, "//label[@data-theme-id='g']")))
        elif AppearanceMode.Terminal_fr == apparence_mode:
            element = wait.until(EC.visibility_of_element_located((By.XPATH, "//label[@data-theme-id='t']")))
        else:
            print("Appearance mode not supported!")
        element.click()
        print("******* Appearance mode changed to '{}' *******".format(apparence_mode))

    def click_button_save_and_exist(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located(SettingsPageLocators.button_save_and_exist_locator))
        element.click()
        print("options are saved/applied !")
