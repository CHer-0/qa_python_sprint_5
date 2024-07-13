from links import Links
from locators import TestLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestRegistration:

    def test_registration_valid_account(self, driver, generate_data):
        driver.get(Links.REGISTER)
        # Дождемся явного ожидания для загрузки кнопки Войти на форме регистрации
        WebDriverWait(driver, 2).until(expected_conditions.presence_of_element_located(TestLocators.ENTER_REGISTER))

        login, password = generate_data["login"], generate_data["password"]
        # Заполним поле "Имя" корректным значением
        driver.find_element(*TestLocators.NAME_REGISTER).send_keys(login)
        # Заполним поле "EMAIL" корректным значением
        driver.find_element(*TestLocators.EMAIL_REGISTER).send_keys(login + '@yandex.ru')
        # Заполним поле "пароль" корректным значением
        driver.find_element(*TestLocators.PASS_REGISTER).send_keys(password)
        # Нажмем кнопку "Войти" с заполненными данными тестовой учетной записи
        driver.find_element(*TestLocators.ENTER_ENTER).click()

        # Дождемся явного ожидания для загрузки формы авторизации
        WebDriverWait(driver, 2).until(expected_conditions.url_matches(Links.LOGIN))

        assert driver.current_url == Links.LOGIN

    def test_registration_pass_less_than_6(self, driver, generate_data):
        driver.get(Links.REGISTER)
        # Дождемся явного ожидания для загрузки кнопки Войти на форме регистрации
        WebDriverWait(driver, 2).until(expected_conditions.presence_of_element_located(TestLocators.ENTER_REGISTER))

        login, password = generate_data["login"], '12345'
        # Заполним поле "Имя" корректным значением
        driver.find_element(*TestLocators.NAME_REGISTER).send_keys(login)
        # Заполним поле "EMAIL" корректным значением
        driver.find_element(*TestLocators.EMAIL_REGISTER).send_keys(login + '@yandex.ru')
        # Заполним поле "пароль" некорректным значением, корочке 6 символов
        driver.find_element(*TestLocators.PASS_REGISTER).send_keys(password)
        # Нажмем кнопку "Войти" с заполненными данными тестовой учетной записи
        driver.find_element(*TestLocators.ENTER_ENTER).click()
        assert driver.find_element(*TestLocators.PASS_WRONG_REGISTER).text == 'Некорректный пароль'

