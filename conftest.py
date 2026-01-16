import pytest
from selenium import webdriver
from data import Urls
from locators import Locators
from data import TestData
from data import Config
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    driver.get(Urls.DESK_URL)

    yield driver

    driver.quit()


@pytest.fixture
def login(driver):
    driver.find_element(*Locators.LOGIN_AND_REGISTRATION_BUTTON).click()

    WebDriverWait(driver, Config.WAIT_TIME).until(EC.visibility_of_element_located(Locators.INPUT_EMAIL))

    driver.find_element(*Locators.INPUT_EMAIL).send_keys(TestData.EXISTING_EMAIL)

    driver.find_element(*Locators.INPUT_PASSWORD).send_keys(TestData.PASSWORD)

    driver.find_element(*Locators.LOGIN_BUTTON).click()

    WebDriverWait(driver, Config.WAIT_TIME).until(EC.visibility_of_element_located(Locators.PROFILE_NAME))