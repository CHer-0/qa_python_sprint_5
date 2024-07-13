from links import Links
from locators import TestLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestPersonalCabToConstructor:

    def test_personal_cab_to_constructor_click(self, driver):
        driver.get(Links.LOGIN)
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

        # Нажмем кнопку "Конструктор"
        driver.find_element(*TestLocators.CONSTRUCTOR).click()
        # Дождемся явного ожидания для загрузки кнопки "Оформить заказ"
        WebDriverWait(driver, 2).until(expected_conditions.presence_of_element_located(TestLocators.ORDER_PLACE))

        assert driver.current_url == Links.MAIN

    def test_personal_cab_to_logo_click(self, driver):
        driver.get(Links.LOGIN)
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
        WebDriverWait(driver, 2).until(
            expected_conditions.presence_of_element_located(TestLocators.EXIT_PERSONAL_CAB))

        # Нажмем кнопку с логотипом
        driver.find_element(*TestLocators.LOGO).click()
        # Дождемся явного ожидания для загрузки кнопки "Оформить заказ"
        WebDriverWait(driver, 2).until(expected_conditions.presence_of_element_located(TestLocators.ORDER_PLACE))

        assert driver.current_url == Links.MAIN
