from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import locators
import helpers
import urls

class TestTransitions:
    def test_transition_to_account_profile(self, driver):
        email, password = helpers.register_new_user(driver)
        helpers.login_with_user(driver, email, password)
        
        driver.find_element(*locators.HEADER_BUTTON_ACCOUNT).click()
        
        # Ожидание внутри assert + используем urls.py
        assert WebDriverWait(driver, 10).until(EC.url_to_be(urls.PROFILE_URL))

    def test_transition_from_profile_to_constructor_button(self, driver):
        email, password = helpers.register_new_user(driver)
        helpers.login_with_user(driver, email, password)
        
        driver.find_element(*locators.HEADER_BUTTON_ACCOUNT).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(urls.PROFILE_URL))
        
        driver.find_element(*locators.HEADER_BUTTON_CONSTRUCTOR).click()
        
        assert WebDriverWait(driver, 10).until(EC.url_to_be(urls.BASE_URL))

    def test_transition_from_profile_to_logo(self, driver):
        email, password = helpers.register_new_user(driver)
        helpers.login_with_user(driver, email, password)
        
        driver.find_element(*locators.HEADER_BUTTON_ACCOUNT).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(urls.PROFILE_URL))
        
        driver.find_element(*locators.HEADER_LOGO).click()
        
        assert WebDriverWait(driver, 10).until(EC.url_to_be(urls.BASE_URL))

    def test_logout_from_profile(self, driver):
        email, password = helpers.register_new_user(driver)
        helpers.login_with_user(driver, email, password)
        
        driver.find_element(*locators.HEADER_BUTTON_ACCOUNT).click()
        
        # Ждем, пока прогрузится профиль и появится кнопка "Выход"
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locators.ACCOUNT_BUTTON_LOGOUT))
        
        driver.find_element(*locators.ACCOUNT_BUTTON_LOGOUT).click()
        
        # Проверяем, что нас выкинуло на страницу авторизации
        assert WebDriverWait(driver, 10).until(EC.url_to_be(urls.LOGIN_URL))
