from selenium import webdriver
from selenium.webdriver.common.by import By

class TestLocators:
    # Главная форма
    # Кнопка "Войти в аккаунт" сразу после первоначальной загрузки открывает форму "Авторизация"
    ENTER_AUTH = By.XPATH, '//button[text()="Войти в аккаунт"]'
    # Кнопка оформить заказ на главной форме
    ORDER_PLACE = By.XPATH, '//button[text()="Оформить заказ"]'
    # Кнопка "Личный кабинет" в правом верхнем углу главной формы
    PERSONAL_CAB = By.XPATH, '//p[text()="Личный Кабинет"]'
    # Кнопка "Конструктор" в левом верхнем углу главной формы
    CONSTRUCTOR = By.XPATH, '//p[text()="Конструктор"]'
    # Кнопка с логотипом в центре сверху главной формы
    LOGO = By.XPATH, '//a[@class="active" and @href="/"]'
    BULKI = By.XPATH, '//span[text()="Булки"]'
    SOUSY = By.XPATH, '//span[text()="Соусы"]'
    NACHINKI = By.XPATH, '//span[text()="Начинки"]'
    SELECTED_SECTION = By.XPATH, '//div[@class="tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"]'

    # Форма "Авторизация"
    # Поле ввода емайла на форме "Авторизация"
    EMAIL_AUTH = By.XPATH, '//input[@name="name"]'
    # Поле ввода пароля на форме "Авторизация"
    PASS_AUTH = By.XPATH, '//input[@name="Пароль"]'
    # Кнопка "Войти" с введенными логином (емайл) и паролем на форме "Авторизация"
    ENTER_ENTER = By.XPATH, '//button[text()="Войти"]'
    # Сообщение о неверном пароле (менее 6 символов)(XPATH = //fieldset[2]/div/p
    PASS_WRONG_AUTH = By.XPATH, '//p[text()="Некорректный пароль"]'

    # Форма "Регистрация"
    # Кнопка "Зарегистрироваться" в форме "Регистрация"
    ENTER_REGISTER = By.XPATH, '//button[text()="Зарегистрироваться"]'
    # Поле ввода имени на форме "Регистрация"
    NAME_REGISTER = By.XPATH, '//div[./label[text()="Имя"]]/input'
    # Поле ввода емайла на форме "Регистрация"
    EMAIL_REGISTER = By.XPATH, '//div[./label[text()="Email"]]/input'
    # Поле ввода пароля на форме "Регистрация"
    PASS_REGISTER = By.XPATH, '//div[./label[text()="Пароль"]]/input'
    # Сообщение о неверном пароле (менее 6 символов)(XPATH = //fieldset[3]/div/p
    PASS_WRONG_REGISTER = By.XPATH, '//p[text()="Некорректный пароль"]'
    # синее слово со ссылкой "Войти"
    BLUE_ENTER = By.XPATH, '//a[@href="/login"]'

    # Форма восстановления забытого пароля
    # синее слово со ссылкой "Войти" = BLUE_ENTER
    # FORGOT_PASS_ENTER = By.XPATH, '//a[@href="/login"]'


    # Форма "Личный кабинет"
    # кнопка "Выход"
    EXIT_PERSONAL_CAB = By.XPATH, '//button[text()="Выход"]'
