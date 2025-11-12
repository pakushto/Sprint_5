from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from data import Config, TestData
from helpers import Helper


class TestDeskRegistration:

    def test_registration(self, driver):
        driver.find_element(*Locators.LOGIN_AND_REGISTRATION_BUTTON).click()

        WebDriverWait(driver, Config.WAIT_TIME).until(EC.visibility_of_element_located(Locators.NO_ACCOUNT_BUTTON))
        
        driver.find_element(*Locators.NO_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, Config.WAIT_TIME).until(EC.visibility_of_element_located(Locators.INPUT_EMAIL))
        
        email_input = driver.find_element(*Locators.INPUT_EMAIL)
        email = Helper.random_email()        
        email_input.send_keys(email)

        password_input = driver.find_element(*Locators.INPUT_PASSWORD)
        password = Helper.random_password()
        password_input.send_keys(password)

        repeat_password_input = driver.find_element(*Locators.INPUT_REPEAT_PASSWORD)
        repeat_password_input.send_keys(password)

        driver.find_element(*Locators.CREATE_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, Config.WAIT_TIME).until(EC.visibility_of_element_located(Locators.PROFILE_IMAGE))

        profile_name = driver.find_element(*Locators.PROFILE_NAME).text
        profile_image = driver.find_element(*Locators.PROFILE_IMAGE)

        assert profile_name == 'User.', f"Ожидалось имя 'User.', но получено '{profile_name}'"
        assert profile_image.is_displayed(), "Аватар пользователя не отображается"


    def test_registration_invalid_email(self, driver):

        driver.find_element(*Locators.LOGIN_AND_REGISTRATION_BUTTON).click()

        WebDriverWait(driver, Config.WAIT_TIME).until(EC.visibility_of_element_located(Locators.NO_ACCOUNT_BUTTON))
        
        driver.find_element(*Locators.NO_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, Config.WAIT_TIME).until(EC.visibility_of_element_located(Locators.INPUT_EMAIL))
        
        email_input = driver.find_element(*Locators.INPUT_EMAIL)
        email = TestData.INVALID_EMAIL
        email_input.send_keys(email)

        password_input = driver.find_element(*Locators.INPUT_PASSWORD)
        password = Helper.random_password()
        password_input.send_keys(password)

        repeat_password_input = driver.find_element(*Locators.INPUT_REPEAT_PASSWORD)
        repeat_password_input.send_keys(password)

        driver.find_element(*Locators.CREATE_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, Config.WAIT_TIME).until(EC.visibility_of_element_located(Locators.EMAIL_ERROR_MESSAGE))

        error_message = driver.find_element(*Locators.EMAIL_ERROR_MESSAGE).text

        count_of_red_inputs = len(driver.find_elements(*Locators.INPUTS_WITH_ERROR))

        assert error_message == 'Ошибка', f"Ожидалось сообщение об ошибке 'Ошибка', но получено '{error_message}'" 
        assert count_of_red_inputs == 3, f"Ожидалось 3 поля с ошибкой, но получено {count_of_red_inputs}"
        

    def test_registration_existing_email(self, driver):

        driver.find_element(*Locators.LOGIN_AND_REGISTRATION_BUTTON).click()

        WebDriverWait(driver, Config.WAIT_TIME).until(EC.visibility_of_element_located(Locators.NO_ACCOUNT_BUTTON))
        
        driver.find_element(*Locators.NO_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, Config.WAIT_TIME).until(EC.visibility_of_element_located(Locators.INPUT_EMAIL))
        
        email_input = driver.find_element(*Locators.INPUT_EMAIL)
        email = TestData.EXISTING_EMAIL
        email_input.send_keys(email)

        password_input = driver.find_element(*Locators.INPUT_PASSWORD)
        password = Helper.random_password()
        password_input.send_keys(password)

        repeat_password_input = driver.find_element(*Locators.INPUT_REPEAT_PASSWORD)
        repeat_password_input.send_keys(password)

        driver.find_element(*Locators.CREATE_ACCOUNT_BUTTON).click()
                
        WebDriverWait(driver, Config.WAIT_TIME).until(EC.visibility_of_element_located(Locators.EMAIL_ERROR_MESSAGE))

        error_message = driver.find_element(*Locators.EMAIL_ERROR_MESSAGE).text

        count_of_red_inputs = len(driver.find_elements(*Locators.INPUTS_WITH_ERROR))

        assert error_message == 'Ошибка', f"Ожидалось сообщение об ошибке 'Ошибка', но получено '{error_message}'" 
        assert count_of_red_inputs == 3, f"Ожидалось 3 поля с ошибкой, но получено {count_of_red_inputs}"