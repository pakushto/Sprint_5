import random
import re
from data import Config
from locators import Locators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Helper: 
    @staticmethod
    def random_email():
        return f"testuser{random.randint(1000,9999)}@example.com"
    
    
    @staticmethod
    def random_password():
        return f"Pass{random.randint(1000,9999)}!"
    
    @staticmethod
    def random_ad_name():
        return f"Ad{random.randint(1000,9999)}"
    

    @staticmethod
    def random_ad_description():
        return f"This is a description #{random.randint(1000,9999)}."
    

    @staticmethod
    def random_ad_price():
        return str(random.randint(100, 10000))


    @staticmethod
    def go_to_last_page(driver, timeout=Config.WAIT_TIME):
        WebDriverWait(driver,Config.WAIT_TIME).until(EC.visibility_of_all_elements_located(Locators.ALL_AD_CARDS_ON_PAGE))    
        while True:
                if driver.find_elements(*Locators.DISABLED_NEXT_PAGE_BUTTON):
                    break
        
                old_cards = driver.find_elements(*Locators.ALL_AD_CARDS_ON_PAGE)
                driver.find_element(*Locators.NEXT_PAGE_BUTTON).click()
                WebDriverWait(driver, timeout).until(EC.staleness_of(old_cards[0]))


    @staticmethod
    def extract_price(price_text: str) -> int:
        digits = re.sub(r"[^\d]", "", price_text)
        return int(digits)