from selenium import webdriver
from selenium.webdriver.common.by import By

class TestLocators:
    # Главная форма
    # Кнопка "Войти в аккаунт" сразу после первоначальной загрузки открывает форму "Авторизация"
    ENTER_AUTH = By.XPATH, '//div/main/section[@class="BurgerConstructor_basket__29Cd7 mt-25 "]/div/button'
    # Кнопка оформить заказ на главной форме
    ORDER_PLACE = By.XPATH, '//div/section/div[@class="Modal_modal_overlay__x2ZCr"]'
    # Кнопка "Личный кабинет" в правом верхнем углу главной формы
    PERSONAL_CAB = By.XPATH, '//div/header/nav/a/p'
    # Кнопка "Конструктор" в левом верхнем углу главной формы
    CONSTRUCTOR = By.XPATH, '//div/header/nav/ul/li/a/p[text()="Конструктор"]'
    # Кнопка с логотипом в центре сверху главной формы
    LOGO = By.XPATH, '//div/header/nav/div/a'
    BULKI = By.XPATH, '//div/main/section/div/div/span[text()="Булки"]'
    SOUSY = By.XPATH, '//div/main/section/div/div/span[text()="Соусы"]'
    NACHINKI = By.XPATH, '//div/main/section/div/div/span[text()="Начинки"]'
    SELECTED_SECTION = By.XPATH, '//div/main/section/div/div[@class="tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"]'

    # Форма "Авторизация"
    # Поле ввода емайла на форме "Авторизация"
    EMAIL_AUTH = By.XPATH, '//div/main/div/form/fieldset/div/div/input[@name="name"]'
    # Поле ввода пароля на форме "Авторизация"
    PASS_AUTH = By.XPATH, '//div/main/div/form/fieldset/div/div/input[@name="Пароль"]'
    # Кнопка "Войти" с введенными логином (емайл) и паролем на форме "Авторизация"
    ENTER_ENTER = By.XPATH, '//div/main/div/form/button'
    # Сообщение о неверном пароле (менее 6 символов)
    PASS_WRONG_AUTH = By.XPATH, '//div/main/div/form/fieldset/div/p'


    # Форма "Регистрация"
    # Кнопка "Зарегистрироваться" в форме "Регистрация"
    ENTER_REGISTER = By.XPATH, '//div/main/div/form/button'
    # Поле ввода имени на форме "Регистрация"
    NAME_REGISTER = By.XPATH, '//div/main/div/form/fieldset/div/div[./label[text()="Имя"]]/input'
    # Поле ввода емайла на форме "Регистрация"
    EMAIL_REGISTER = By.XPATH, '//div/main/div/form/fieldset/div/div[./label[text()="Email"]]/input'
    # Поле ввода пароля на форме "Регистрация"
    PASS_REGISTER = By.XPATH, '//div/main/div/form/fieldset/div/div[./label[text()="Пароль"]]/input'
    # Сообщение о неверном пароле (менее 6 символов)
    PASS_WRONG_REGISTER = By.XPATH, '//div/main/div/form/fieldset/div/p[text()="Некорректный пароль"]'
    # синее слово со ссылкой "Войти"
    BLUE_ENTER = By.XPATH, '//div/main/div/div/p/a'

    # Форма восстановления забытого пароля
    # синее слово со ссылкой "Войти" = BLUE_ENTER
    # FORGOT_PASS_ENTER = By.XPATH, '//div/main/div/div/p/a'


    # Форма "Личный кабинет"
    # кнопка "Выход"
    EXIT_PERSONAL_CAB = By.XPATH, '//div/main/div/nav/ul/li/button[text()="Выход"]'



