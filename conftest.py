import pytest
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


@pytest.fixture()
def driver():
    options = Options()
    service = Service()
    options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


@pytest.fixture
def generate_data():
    # Пусть тестовый логин будет содержать от 3 до 8 букв и от 3 до 8 цифр в случайном порядке
    n = random.randint(3, 5)
    login = ''.join([random.choice(list('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')) for x in range(n)])
    n = random.randint(3, 5)
    login += ''.join([random.choice(list('1234567890')) for x in range(n)])

    random.shuffle(list(login)) # Генерирует логин
    n = random.randint(6, 10)
    # Пусть тестовый пароль будет содержать от 6 до 10 цифр в случайном порядке
    password = ''.join([random.choice(list('1234567890')) for x in range(n)]) # Назначает пароль
    return {"login": login, "password": password} # Возвращает логин и пароль
