# === СТРАНИЦА РЕГИСТРАЦИИ (/register) ===
REG_NAME_INPUT = ("xpath", "//input[@name='name']")
REG_EMAIL_INPUT = ("xpath", "//label[text()='Email']/following-sibling::input")
REG_PASSWORD_INPUT = ("xpath", "//input[@name='Пароль']")
REG_BUTTON_SUBMIT = ("xpath", "//button[text()='Зарегистрироваться']")
REG_ERROR_PASSWORD = ("xpath", "//p[text()='Некорректный пароль']")
REG_LINK_LOGIN = ("xpath", "//a[@href='/login']")

# === ГЛАВНАЯ СТРАНИЦА (/) ===
MAIN_BUTTON_LOGIN = ("xpath", "//button[text()='Войти в аккаунт']")

# --- Вкладки конструктора ---
TAB_BUNS = ("xpath", "//span[text()='Булки']/parent::div")
TAB_SAUCES = ("xpath", "//span[text()='Соусы']/parent::div")
TAB_FILLINGS = ("xpath", "//span[text()='Начинки']/parent::div")

# === ОБЩИЕ ЭЛЕМЕНТЫ (Шапка сайта) ===
HEADER_BUTTON_ACCOUNT = ("xpath", "//a[@href='/account']")
HEADER_LOGO = ("xpath", "//div[contains(@class, 'logo')]")
HEADER_BUTTON_CONSTRUCTOR = ("xpath", "//p[text()='Конструктор']/parent::a")

# === СТРАНИЦА ВХОДА (/login) ===
LOGIN_EMAIL_INPUT = ("xpath", "//input[@name='name']") 
LOGIN_PASSWORD_INPUT = ("xpath", "//input[@name='Пароль']")
LOGIN_BUTTON_SUBMIT = ("xpath", "//button[contains(text(), 'Войти')]")

# === СТРАНИЦА ВОССТАНОВЛЕНИЯ ПАРОЛЯ (/forgot-password) ===
FORGOT_LINK_LOGIN = ("xpath", "//a[@href='/login']")

# === ЛИЧНЫЙ КАБИНЕТ (/account/profile) ===
ACCOUNT_BUTTON_LOGOUT = ("xpath", "//button[text()='Выход']")

# Заголовки разделов внутри конструктора
HEADER_BUNS = ("xpath", "//h2[text()='Булки']")
HEADER_SAUCES = ("xpath", "//h2[text()='Соусы']")
HEADER_FILLINGS = ("xpath", "//h2[text()='Начинки']")
