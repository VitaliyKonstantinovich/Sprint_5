from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import locators
import helpers
import urls

class TestLogin:
    def test_login_from_main_page_button(self, driver):
        email, password = helpers.register_new_user(driver)
        
        driver.get(urls.BASE_URL)
        driver.find_element(*locators.MAIN_BUTTON_LOGIN).click()
        helpers.login_with_user(driver, email, password)
        
        # Исправление от ревьюера: ожидание в ассерте
        assert WebDriverWait(driver, 10).until(EC.url_to_be(urls.BASE_URL))

    def test_login_from_header_account_button(self, driver):
        email, password = helpers.register_new_user(driver)
        
        driver.get(urls.BASE_URL)
        driver.find_element(*locators.HEADER_BUTTON_ACCOUNT).click()
        helpers.login_with_user(driver, email, password)
        
        assert WebDriverWait(driver, 10).until(EC.url_to_be(urls.BASE_URL))

    def test_login_from_registration_form_link(self, driver):
        email, password = helpers.register_new_user(driver)
        
        driver.get(urls.REGISTER_URL)
        driver.find_element(*locators.REG_LINK_LOGIN).click()
        helpers.login_with_user(driver, email, password)
        
        assert WebDriverWait(driver, 10).until(EC.url_to_be(urls.BASE_URL))

    def test_login_from_forgot_password_link(self, driver):
        email, password = helpers.register_new_user(driver)
        
        driver.get(urls.FORGOT_PASSWORD_URL)
        driver.find_element(*locators.FORGOT_LINK_LOGIN).click()
        helpers.login_with_user(driver, email, password)
        
        assert WebDriverWait(driver, 10).until(EC.url_to_be(urls.BASE_URL))
