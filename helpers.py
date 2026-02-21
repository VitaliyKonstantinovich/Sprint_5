import random

def generate_random_email():
    random_digits = random.randint(100, 999)
    # Формат по ТЗ: имя_фамилия_номер когорты_любые 3 цифры@домен
    return f"vitaliy_glebov_39_{random_digits}@yandex.ru"

def generate_random_password():
    random_numbers = random.randint(100000, 999999)
    return f"pass{random_numbers}"

def generate_wrong_password():
    random_numbers = random.randint(100, 999)
    return str(random_numbers)
