import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    # устанавливаем драйвер для Chrome
    service = Service(ChromeDriverManager().install())
    
    # открываем браузер
    driver = webdriver.Chrome(service=service)
    
    # разворачиваем окно на весь экран
    driver.maximize_window()
    
    # передаем браузер в тест
    yield driver
    
    # закрываем браузер после того, как тест отработает
    driver.quit()
