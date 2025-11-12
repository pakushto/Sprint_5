from selenium.webdriver.common.by import By


class Locators:
    LOGIN_AND_REGISTRATION_BUTTON = (By.XPATH, "//button[text()='Вход и регистрация']")
    NO_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Нет аккаунта']")
    INPUT_EMAIL = (By.XPATH, "//input[@placeholder='Введите Email']")
    INPUT_PASSWORD = (By.XPATH, "//input[@placeholder='Пароль']")
    INPUT_REPEAT_PASSWORD = (By.XPATH, "//input[@placeholder='Повторите пароль']")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Создать аккаунт']")
    PROFILE_NAME = (By.XPATH, "//h3[contains(@class, 'profileText name')]")
    PROFILE_IMAGE = (By.XPATH, "//*[local-name()='svg' and @class='svgSmall']")
    EMAIL_ERROR_MESSAGE = (By.XPATH, "//input[@name='email']/ancestor::div/following-sibling::span")
    INPUTS_WITH_ERROR = (By.XPATH, "//div[contains(@class, 'input_inputError')]")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выйти']")
    ADD_AD_BUTTON = (By.XPATH, "//button[text()='Разместить объявление']")
    CREATE_AD_FORM_TITLE = (By.XPATH, "//h1[text()='Новое объявление']")
    AUTH_POPUP_TITLE = (By.XPATH, "//h1[contains(text(),'Чтобы разместить объявление, авторизуйтесь')]")
    AD_NAME_INPUT = (By.XPATH, "//input[@placeholder='Название']")
    AD_DESCRIPTION_INPUT = (By.XPATH, "//textarea[@placeholder='Описание товара']")
    AD_PRICE_INPUT = (By.XPATH, "//input[@placeholder='Стоимость']")
    DROPDOWN_MENU_CATEGORY = (By.XPATH, ".//input[@name='category']/following-sibling::button")
    CATEGORY_BOOKS = (By.XPATH, ".//input[@name='category']/parent::div/following::span[text()='Книги']/parent::button")
    DROPDOWN_MENU_CITY = (By.XPATH, ".//input[@name='city']/following-sibling::button")
    CITY_EKATERINBURG = (By.XPATH, ".//input[@name='city']/parent::div/following::span[text()='Екатеринбург']/parent::button")
    USED_CONDITION_RADIO = (By.XPATH, "//input[@name='condition' and @value='Б/У']/following-sibling::div")
    SUBMIT_AD_BUTTON = (By.XPATH, "//button[text()='Опубликовать']")
    USER_PROFILE_BUTTON = (By.XPATH, "//button[@class='circleSmall']")
    ADS_IN_PROFILE_TITLE = (By.XPATH, "//h1[text()='Мои объявления']")
    NAME_OF_LAST_AD_CARD_ON_PAGE = (By.XPATH, "//div[@class='card'][last()]/descendant::div[@class='about']/h2")
    PRICE_OF_LAST_AD_CARD_ON_PAGE = (By.XPATH, "//div[@class='card'][last()]/descendant::div[@class='price']/h2")
    ALL_AD_CARDS_ON_PAGE = (By.XPATH, "//div[@class='card']")
    NEXT_PAGE_BUTTON = (By.XPATH, "//h1[text()='Мои объявления']/following::button[contains(@class, 'arrowButton--right') and not (@disabled)]")
    DISABLED_NEXT_PAGE_BUTTON = (By.XPATH, "//button[contains(@class, 'arrowButton--right') and @disabled]")




