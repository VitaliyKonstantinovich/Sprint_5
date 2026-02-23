import random
import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import locators
import urls


def generate_random_email():
    # Формат по ТЗ: имя_фамилия_номер когорты_любые 3 цифры@домен
    # Чтобы email был уникальным, "вплетаем" время в фамилию (это не запрещено),
    # а 3 цифры оставляем последним блоком.
    stamp = int(time.time())  # секунды
    digits = random.randint(100, 999)
    return f"vitaliy_glebov{stamp}_39_{digits}@yandex.ru".lower()


def generate_random_password():
    # Пароль минимум 6 символов
    rnd = random.randint(100000, 999999)
    return f"pass{rnd}"


def generate_wrong_password():
    # Некорректный пароль (меньше 6 символов)
    return "12345"


def register_new_user(driver):
    """
    Регистрируем нового пользователя и возвращаем email+password.
    Иногда сайт может не перекинуть на /login (например, если email уже занят),
    поэтому делаем несколько попыток с новым email.
    """
    for _ in range(3):
        email = generate_random_email()
        password = generate_random_password()

        driver.get(urls.REGISTER_URL)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locators.REG_NAME_INPUT))

        driver.find_element(*locators.REG_NAME_INPUT).clear()
        driver.find_element(*locators.REG_NAME_INPUT).send_keys("Виталий")

        driver.find_element(*locators.REG_EMAIL_INPUT).clear()
        driver.find_element(*locators.REG_EMAIL_INPUT).send_keys(email)

        driver.find_element(*locators.REG_PASSWORD_INPUT).clear()
        driver.find_element(*locators.REG_PASSWORD_INPUT).send_keys(password)

        driver.find_element(*locators.REG_BUTTON_SUBMIT).click()

        # Ждем, что нас перекинуло на логин (или появилась кнопка "Войти")
        try:
            WebDriverWait(driver, 5).until(EC.url_contains("login"))
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locators.LOGIN_BUTTON_SUBMIT))
            return email, password
        except Exception:
            # Не получилось — пробуем другой email
            continue

    raise AssertionError("Не удалось зарегистрировать пользователя за 3 попытки")


def login_with_user(driver, email, password):
    driver.get(urls.LOGIN_URL)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locators.LOGIN_BUTTON_SUBMIT))

    driver.find_element(*locators.LOGIN_EMAIL_INPUT).clear()
    driver.find_element(*locators.LOGIN_EMAIL_INPUT).send_keys(email)

    driver.find_element(*locators.LOGIN_PASSWORD_INPUT).clear()
    driver.find_element(*locators.LOGIN_PASSWORD_INPUT).send_keys(password)

    driver.find_element(*locators.LOGIN_BUTTON_SUBMIT).click()