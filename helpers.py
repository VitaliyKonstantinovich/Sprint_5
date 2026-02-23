import random
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import locators
import urls

def generate_random_email():
    random_digits = random.randint(100, 999)
    return f"vitaliy_glebov_39_{random_digits}@yandex.ru"

def generate_random_password():
    random_numbers = random.randint(100000, 999999)
    return f"pass{random_numbers}"

def generate_wrong_password():
    random_numbers = random.randint(100, 999)
    return str(random_numbers)

# --- Перенесенные помощники для тестов ---
def register_new_user(driver):
    email = generate_random_email()
    password = generate_random_password()
    
    driver.get(urls.REGISTER_URL)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locators.REG_NAME_INPUT))
    
    driver.find_element(*locators.REG_NAME_INPUT).send_keys("Виталий Глебов")
    driver.find_element(*locators.REG_EMAIL_INPUT).send_keys(email)
    driver.find_element(*locators.REG_PASSWORD_INPUT).send_keys(password)
    driver.find_element(*locators.REG_BUTTON_SUBMIT).click()
    
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locators.LOGIN_BUTTON_SUBMIT))
    return email, password

def login_with_user(driver, email, password):
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locators.LOGIN_BUTTON_SUBMIT))
    driver.find_element(*locators.LOGIN_EMAIL_INPUT).send_keys(email)
    driver.find_element(*locators.LOGIN_PASSWORD_INPUT).send_keys(password)
    driver.find_element(*locators.LOGIN_BUTTON_SUBMIT).click()
