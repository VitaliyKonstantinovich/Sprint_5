from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import locators
import helpers

class TestRegistration:
    def test_successful_registration(self, driver):
        # 1. Открываем страницу регистрации
        driver.get("https://stellarburgers.education-services.ru/register")
        
        # 2. Ждем, пока поле "Имя" появится на странице (чтобы убедиться, что сайт загрузился)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locators.REG_NAME_INPUT))
        
        # 3. Генерируем уникальные данные через наших помощников
        email = helpers.generate_random_email()
        password = helpers.generate_random_password()
        
        # 4. Вводим данные
        driver.find_element(*locators.REG_NAME_INPUT).send_keys("Виталий")
        driver.find_element(*locators.REG_EMAIL_INPUT).send_keys(email)
        driver.find_element(*locators.REG_PASSWORD_INPUT).send_keys(password)
        
        # 5. Нажимаем "Зарегистрироваться"
        driver.find_element(*locators.REG_BUTTON_SUBMIT).click()
        
        # 6. Проверяем, что регистрация прошла успешно
        # По логике сайта, после регистрации нас перекидывает на страницу входа.
        # Поэтому мы ждем, пока в адресной строке появится слово 'login'
        WebDriverWait(driver, 10).until(EC.url_contains("login"))
        assert "login" in driver.current_url

    def test_registration_with_short_password(self, driver):
        # 1. Открываем страницу регистрации
        driver.get("https://stellarburgers.education-services.ru/register")
        
        # 2. Ждем поле "Имя"
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locators.REG_NAME_INPUT))
        
        # 3. Генерируем уникальный email и КОРОТКИЙ (некорректный) пароль
        email = helpers.generate_random_email()
        short_password = helpers.generate_wrong_password()
        
        # 4. Вводим данные
        driver.find_element(*locators.REG_NAME_INPUT).send_keys("Виталий")
        driver.find_element(*locators.REG_EMAIL_INPUT).send_keys(email)
        driver.find_element(*locators.REG_PASSWORD_INPUT).send_keys(short_password)
        
        # 5. Нажимаем "Зарегистрироваться"
        driver.find_element(*locators.REG_BUTTON_SUBMIT).click()
        
        # 6. Проверяем, что появилась ошибка "Некорректный пароль"
        # Мы ждем появления этого текста, и если он появился — тест пройден!
        error_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(locators.REG_ERROR_PASSWORD)
        )
        assert error_message.is_displayed()
