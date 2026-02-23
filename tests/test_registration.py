from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import locators
import helpers
import urls

class TestRegistration:
    def test_successful_registration(self, driver):
        driver.get(urls.REGISTER_URL)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locators.REG_NAME_INPUT))
        
        email = helpers.generate_random_email()
        password = helpers.generate_random_password()
        
        driver.find_element(*locators.REG_NAME_INPUT).send_keys("Виталий")
        driver.find_element(*locators.REG_EMAIL_INPUT).send_keys(email)
        driver.find_element(*locators.REG_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*locators.REG_BUTTON_SUBMIT).click()
        
        # Исправление от ревьюера: Ожидание прямо внутри assert
        assert WebDriverWait(driver, 10).until(EC.url_contains("login"))

    def test_registration_with_short_password(self, driver):
        driver.get(urls.REGISTER_URL)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locators.REG_NAME_INPUT))
        
        email = helpers.generate_random_email()
        short_password = helpers.generate_wrong_password()
        
        driver.find_element(*locators.REG_NAME_INPUT).send_keys("Виталий")
        driver.find_element(*locators.REG_EMAIL_INPUT).send_keys(email)
        driver.find_element(*locators.REG_PASSWORD_INPUT).send_keys(short_password)
        driver.find_element(*locators.REG_BUTTON_SUBMIT).click()
        
        # Исправление от ревьюера: Ожидание прямо внутри assert
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(locators.REG_ERROR_PASSWORD)
        ).is_displayed()
