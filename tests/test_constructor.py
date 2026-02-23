from selenium.webdriver.support.wait import WebDriverWait
import locators
import urls

class TestConstructor:
    def test_transition_to_buns(self, driver):
        driver.get(urls.BASE_URL)
        
        # Кликаем на "Соусы", чтобы уйти с вкладки "Булки"
        driver.find_element(*locators.TAB_SAUCES).click()
        
        # Ждем, пока у Соусов появится класс current
        WebDriverWait(driver, 10).until(
            lambda d: "current" in d.find_element(*locators.TAB_SAUCES).get_attribute("class")
        )
        
        # Кликаем на "Булки"
        driver.find_element(*locators.TAB_BUNS).click()
        
        # Исправление от ревьюера: Проверяем наличие класса 'current', ожидание внутри assert
        assert WebDriverWait(driver, 10).until(
            lambda d: "current" in d.find_element(*locators.TAB_BUNS).get_attribute("class")
        )

    def test_transition_to_sauces(self, driver):
        driver.get(urls.BASE_URL)
        
        driver.find_element(*locators.TAB_SAUCES).click()
        
        assert WebDriverWait(driver, 10).until(
            lambda d: "current" in d.find_element(*locators.TAB_SAUCES).get_attribute("class")
        )

    def test_transition_to_fillings(self, driver):
        driver.get(urls.BASE_URL)
        
        driver.find_element(*locators.TAB_FILLINGS).click()
        
        assert WebDriverWait(driver, 10).until(
            lambda d: "current" in d.find_element(*locators.TAB_FILLINGS).get_attribute("class")
        )