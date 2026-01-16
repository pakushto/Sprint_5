from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from data import Config, TestData


class TestDeskLogin:

    def test_login(self, driver):

        driver.find_element(*Locators.LOGIN_AND_REGISTRATION_BUTTON).click()

        WebDriverWait(driver, Config.WAIT_TIME).until(EC.visibility_of_element_located(Locators.INPUT_EMAIL))

        driver.find_element(*Locators.INPUT_EMAIL).send_keys(TestData.EXISTING_EMAIL)

        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(TestData.PASSWORD)

        driver.find_element(*Locators.LOGIN_BUTTON).click()

        WebDriverWait(driver, Config.WAIT_TIME).until(EC.visibility_of_element_located(Locators.PROFILE_NAME))

        profile_name = driver.find_element(*Locators.PROFILE_NAME).text
        profile_image = driver.find_element(*Locators.PROFILE_IMAGE)

        assert profile_name == 'User.', f"Ожидалось имя 'User.', но получено '{profile_name}'"
        assert profile_image.is_displayed(), "Аватар пользователя не отображается"


    