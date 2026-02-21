from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import locators
import helpers

class TestTransitions:
    # --- Помощник: Регистрация и Вход ---
    # Чтобы зайти в личный кабинет, нам нужно сначала авторизоваться.
    def _register_and_login(self, driver):
        email = helpers.generate_random_email()
        password = helpers.generate_random_password()
        
        # 1. Быстрая регистрация
        driver.get("https://stellarburgers.education-services.ru/register")
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locators.REG_NAME_INPUT))
        driver.find_element(*locators.REG_NAME_INPUT).send_keys("Виталий Глебов")
        driver.find_element(*locators.REG_EMAIL_INPUT).send_keys(email)
        driver.find_element(*locators.REG_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*locators.REG_BUTTON_SUBMIT).click()
        
        # 2. Быстрый вход
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locators.LOGIN_BUTTON_SUBMIT))
        driver.find_element(*locators.LOGIN_EMAIL_INPUT).send_keys(email)
        driver.find_element(*locators.LOGIN_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*locators.LOGIN_BUTTON_SUBMIT).click()
        
        # Ждем загрузки главной страницы
        WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.education-services.ru/"))

    # === ТЕСТЫ ПЕРЕХОДОВ ===

    def test_transition_to_account_profile(self, driver):
        self._register_and_login(driver)
        
        # Кликаем на "Личный Кабинет"
        driver.find_element(*locators.HEADER_BUTTON_ACCOUNT).click()
        
        # Проверяем, что URL изменился на страницу профиля
        WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.education-services.ru/account/profile"))
        assert driver.current_url == "https://stellarburgers.education-services.ru/account/profile"

    def test_transition_from_profile_to_constructor_button(self, driver):
        self._register_and_login(driver)
        
        # Сначала заходим в профиль
        driver.find_element(*locators.HEADER_BUTTON_ACCOUNT).click()
        WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.education-services.ru/account/profile"))
        
        # Кликаем на "Конструктор"
        driver.find_element(*locators.HEADER_BUTTON_CONSTRUCTOR).click()
        
        # Проверяем, что вернулись на главную страницу
        WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.education-services.ru/"))
        assert driver.current_url == "https://stellarburgers.education-services.ru/"

    def test_transition_from_profile_to_logo(self, driver):
        self._register_and_login(driver)
        
        # Сначала заходим в профиль
        driver.find_element(*locators.HEADER_BUTTON_ACCOUNT).click()
        WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.education-services.ru/account/profile"))
        
        # Кликаем на огромный Логотип по центру шапки
        driver.find_element(*locators.HEADER_LOGO).click()
        
        # Проверяем, что вернулись на главную
        WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.education-services.ru/"))
        assert driver.current_url == "https://stellarburgers.education-services.ru/"

    # === ТЕСТ ВЫХОДА ===
    def test_logout_from_profile(self, driver):
        self._register_and_login(driver)
        
        # Заходим в профиль
        driver.find_element(*locators.HEADER_BUTTON_ACCOUNT).click()
        
        # Ждем, пока прогрузится профиль и появится кнопка "Выход"
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locators.ACCOUNT_BUTTON_LOGOUT))
        
        # Кликаем "Выход"
        driver.find_element(*locators.ACCOUNT_BUTTON_LOGOUT).click()
        
        # Проверяем, что нас выкинуло на страницу авторизации /login
        WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.education-services.ru/login"))
        assert driver.current_url == "https://stellarburgers.education-services.ru/login"
