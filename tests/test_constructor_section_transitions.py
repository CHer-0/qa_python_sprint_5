from links import Links
from locators import TestLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestConstructorSectionTransitions:

    def test_constructor_select_sousy(self, driver):
        driver.get(Links.LOGIN)
        # Дождемся явного ожидания для загрузки кнопки Войти на форме авторизации
        WebDriverWait(driver, 2).until(expected_conditions.presence_of_element_located(TestLocators.ENTER_ENTER))

        # Нажмем кнопку "Конструктор"
        driver.find_element(*TestLocators.CONSTRUCTOR).click()
        # Дождемся явного ожидания для загрузки кнопки "Оформить заказ"
        WebDriverWait(driver, 2).until(expected_conditions.presence_of_element_located(TestLocators.ORDER_PLACE))

        # Нажмем раздел "Соусы" в меню "Конструктор"
        driver.find_element(*TestLocators.SOUSY).click()

        assert driver.find_element(*TestLocators.SELECTED_SECTION).text == 'Соусы'

    def test_constructor_select_nachinki(self, driver):
        driver.get(Links.LOGIN)
        # Дождемся явного ожидания для загрузки кнопки Войти на форме авторизации
        WebDriverWait(driver, 2).until(expected_conditions.presence_of_element_located(TestLocators.ENTER_ENTER))

        # Нажмем кнопку "Конструктор"
        driver.find_element(*TestLocators.CONSTRUCTOR).click()
        # Дождемся явного ожидания для загрузки кнопки "Оформить заказ"
        WebDriverWait(driver, 2).until(expected_conditions.presence_of_element_located(TestLocators.ORDER_PLACE))

        # Нажмем раздел "Начинки" в меню "Конструктор"
        driver.find_element(*TestLocators.NACHINKI).click()

        assert driver.find_element(*TestLocators.SELECTED_SECTION).text == 'Начинки'

    def test_constructor_select_bulki(self, driver):
        driver.get(Links.LOGIN)
        # Дождемся явного ожидания для загрузки кнопки Войти на форме авторизации
        WebDriverWait(driver, 2).until(expected_conditions.presence_of_element_located(TestLocators.ENTER_ENTER))

        # Нажмем кнопку "Конструктор"
        driver.find_element(*TestLocators.CONSTRUCTOR).click()
        # Дождемся явного ожидания для загрузки кнопки "Оформить заказ"
        WebDriverWait(driver, 2).until(expected_conditions.presence_of_element_located(TestLocators.ORDER_PLACE))

        # Нажмем раздел "Начинки" в меню "Конструктор"
        driver.find_element(*TestLocators.NACHINKI).click()
        # Нажмем раздел "Булки" в меню "Конструктор"
        driver.find_element(*TestLocators.BULKI).click()

        assert driver.find_element(*TestLocators.SELECTED_SECTION).text == 'Булки'
