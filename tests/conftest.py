import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    # открываем браузер Chrome
    driver = webdriver.Chrome()

    # разворачиваем окно на весь экран
    driver.maximize_window()

    # передаем браузер в тест
    yield driver

    # закрываем браузер после того, как тест отработает
    driver.quit()