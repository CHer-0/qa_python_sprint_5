import pytest
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from locators import TestLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


@pytest.fixture()
def driver():
    options = Options()
    #service = Service(executable_path='\Users\1\PycharmProjects\qa_python_sprint_5')
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

@pytest.fixture
def load_to_constructor(driver, url):
    driver.get(url + 'login')
    # Дождемся явного ожидания для загрузки кнопки Войти на форме авторизации
    WebDriverWait(driver, 2).until(expected_conditions.presence_of_element_located(TestLocators.ENTER_ENTER))
    # Зайдем под уже созданной учетной записью
    login, password = 'vivrus', '123456'
    # Заполним поле "EMAIL" корректным значением
    driver.find_element(*TestLocators.EMAIL_AUTH).send_keys(login + '@yandex.ru')
    # Заполним поле "пароль" корректным значением
    driver.find_element(*TestLocators.PASS_AUTH).send_keys(password)
    # Нажмем кнопку "Войти" с заполненными данными тестовой учетной записи
    driver.find_element(*TestLocators.ENTER_ENTER).click()
    # Дождемся явного ожидания для загрузки кнопки "Личный кабинет"
    WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(TestLocators.PERSONAL_CAB))

    # Нажмем кнопку "Личный кабинет"
    driver.find_element(*TestLocators.PERSONAL_CAB).click()
    # Дождемся явного ожидания для загрузки кнопки Выйти на форме "Личный кабинет"
    WebDriverWait(driver, 2).until(expected_conditions.presence_of_element_located(TestLocators.EXIT_PERSONAL_CAB))
    return driver
