from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import locators
import helpers

class TestLogin:
    # --- НОВЫЙ ПОМОЩНИК: Быстрая регистрация перед тестом ---
    def _register_new_user(self, driver):
        email = helpers.generate_random_email()
        password = helpers.generate_random_password()
        
        # Робот быстро регает пользователя
        driver.get("https://stellarburgers.education-services.ru/register")
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locators.REG_NAME_INPUT))
        
        driver.find_element(*locators.REG_NAME_INPUT).send_keys("Виталий Глебов")
        driver.find_element(*locators.REG_EMAIL_INPUT).send_keys(email)
        driver.find_element(*locators.REG_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*locators.REG_BUTTON_SUBMIT).click()
        
        # Ждем, пока сайт перекинет нас на страницу входа
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locators.LOGIN_BUTTON_SUBMIT))
        
        # Возвращаем созданные email и пароль, чтобы тест мог под ними войти
        return email, password

    # --- Помощник: заполнение формы входа ---
    def _login_with_user(self, driver, email, password):
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locators.LOGIN_BUTTON_SUBMIT))
        
        driver.find_element(*locators.LOGIN_EMAIL_INPUT).send_keys(email)
        driver.find_element(*locators.LOGIN_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*locators.LOGIN_BUTTON_SUBMIT).click()
        
        WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.education-services.ru/"))
        assert driver.current_url == "https://stellarburgers.education-services.ru/"


    # === САМИ ТЕСТЫ ===

    def test_login_from_main_page_button(self, driver):
        # 1. Регистрируем свежего юзера
        email, password = self._register_new_user(driver)
        
        # 2. Идем на главную страницу, как просят в ТЗ
        driver.get("https://stellarburgers.education-services.ru/")
        driver.find_element(*locators.MAIN_BUTTON_LOGIN).click()
        
        # 3. Входим под созданным юзером
        self._login_with_user(driver, email, password)

    def test_login_from_header_account_button(self, driver):
        email, password = self._register_new_user(driver)
        
        driver.get("https://stellarburgers.education-services.ru/")
        driver.find_element(*locators.HEADER_BUTTON_ACCOUNT).click()
        
        self._login_with_user(driver, email, password)

    def test_login_from_registration_form_link(self, driver):
        email, password = self._register_new_user(driver)
        
        driver.get("https://stellarburgers.education-services.ru/register")
        driver.find_element(*locators.REG_LINK_LOGIN).click()
        
        self._login_with_user(driver, email, password)

    def test_login_from_forgot_password_link(self, driver):
        email, password = self._register_new_user(driver)
        
        driver.get("https://stellarburgers.education-services.ru/forgot-password")
        driver.find_element(*locators.FORGOT_LINK_LOGIN).click()
        
        self._login_with_user(driver, email, password)
