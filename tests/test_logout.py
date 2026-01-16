from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from data import Config, TestData

class TestDeskLogout:

    def test_logout(self, driver, login):

        driver.find_element(*Locators.LOGOUT_BUTTON).click()

        WebDriverWait(driver, Config.WAIT_TIME).until(EC.visibility_of_element_located(Locators.LOGIN_AND_REGISTRATION_BUTTON))

        profile_name = driver.find_elements(*Locators.PROFILE_NAME)
        registration_button = driver.find_element(*Locators.LOGIN_AND_REGISTRATION_BUTTON)

        assert not profile_name 
        assert registration_button.is_displayed()