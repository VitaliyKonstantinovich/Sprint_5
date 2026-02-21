from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import locators

class TestConstructor:
    # --- ТЕСТ 1: Переход к разделу «Булки» ---
    def test_transition_to_buns(self, driver):
        driver.get("https://stellarburgers.education-services.ru/")
        
        # Кликаем на "Соусы", чтобы прокрутить страницу вниз
        driver.find_element(*locators.TAB_SAUCES).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locators.HEADER_SAUCES))
        
        # Теперь кликаем на "Булки", чтобы вернуться наверх
        driver.find_element(*locators.TAB_BUNS).click()
        
        # Проверяем, что заголовок "Булки" стал виден на экране
        # (он может быть перекрыт другим элементом, поэтому ждем именно visibility)
        buns_header = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(locators.HEADER_BUNS)
        )
        assert buns_header.is_displayed()

    # --- ТЕСТ 2: Переход к разделу «Соусы» ---
    def test_transition_to_sauces(self, driver):
        driver.get("https://stellarburgers.education-services.ru/")
        
        # Кликаем на "Соусы"
        driver.find_element(*locators.TAB_SAUCES).click()
        
        # Проверяем, что заголовок "Соусы" появился и виден
        sauces_header = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(locators.HEADER_SAUCES)
        )
        assert sauces_header.is_displayed()

    # --- ТЕСТ 3: Переход к разделу «Начинки» ---
    def test_transition_to_fillings(self, driver):
        driver.get("https://stellarburgers.education-services.ru/")
        
        # Кликаем на "Начинки"
        driver.find_element(*locators.TAB_FILLINGS).click()
        
        # Проверяем, что заголовок "Начинки" появился и виден
        fillings_header = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(locators.HEADER_FILLINGS)
        )
        assert fillings_header.is_displayed()
