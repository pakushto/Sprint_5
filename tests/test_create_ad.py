from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from data import Config, TestData
from helpers import Helper

class TestDeskAddingAd:

    def test_create_ad_with_unauthorized_user(self, driver):

        driver.find_element(*Locators.ADD_AD_BUTTON).click()

        WebDriverWait(driver, Config.WAIT_TIME).until(EC.visibility_of_element_located(Locators.AUTH_POPUP_TITLE))

        auth_popup_title = driver.find_element(*Locators.AUTH_POPUP_TITLE).text
        assert auth_popup_title == 'Чтобы разместить объявление, авторизуйтесь'
        
    def test_create_ad_with_authorized_user(self, driver, login):

        driver.find_element(*Locators.ADD_AD_BUTTON).click()

        WebDriverWait(driver, Config.WAIT_TIME).until(EC.visibility_of_element_located(Locators.CREATE_AD_FORM_TITLE))

        ad_name_input = driver.find_element(*Locators.AD_NAME_INPUT)
        ad_name = Helper.random_ad_name()
        ad_name_input.send_keys(ad_name)

        ad_description_input = driver.find_element(*Locators.AD_DESCRIPTION_INPUT)
        ad_description = Helper.random_ad_description()
        ad_description_input.send_keys(ad_description)

        ad_price_input = driver.find_element(*Locators.AD_PRICE_INPUT)
        ad_price = Helper.random_ad_price()
        ad_price_input.send_keys(ad_price)

        driver.find_element(*Locators.DROPDOWN_MENU_CATEGORY).click()
        driver.find_element(*Locators.CATEGORY_BOOKS).click()

        driver.find_element(*Locators.DROPDOWN_MENU_CITY).click()
        driver.find_element(*Locators.CITY_EKATERINBURG).click()

        driver.find_element(*Locators.USED_CONDITION_RADIO).click()

        driver.find_element(*Locators.SUBMIT_AD_BUTTON).click()

        WebDriverWait(driver, Config.WAIT_TIME).until(EC.visibility_of_any_elements_located(Locators.ALL_AD_CARDS_ON_PAGE))

        driver.find_element(*Locators.USER_PROFILE_BUTTON).click()
        
        WebDriverWait(driver, Config.WAIT_TIME).until(EC.visibility_of_element_located(Locators.ADS_IN_PROFILE_TITLE))
        
        Helper.go_to_last_page(driver)

        current_ad_price = driver.find_element(*Locators.PRICE_OF_LAST_AD_CARD_ON_PAGE).text
        current_ad_name = driver.find_element(*Locators.NAME_OF_LAST_AD_CARD_ON_PAGE).text

        assert  current_ad_name == ad_name, "Название объявления не совпадает"
        assert Helper.extract_price(current_ad_price) == int(ad_price), "Цена объявления не совпадает"
