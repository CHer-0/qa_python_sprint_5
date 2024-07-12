from selenium import webdriver
from selenium.webdriver.common.by import By

class TestLocators:
    # Главная форма
    # Кнопка "Войти в аккаунт" сразу после первоначальной загрузки открывает форму "Авторизация"
    ENTER_AUTH = By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button'
    # Кнопка оформить заказ на главной форме
    ORDER_PLACE = By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button'
    # Кнопка "Личный кабинет" в правом верхнем углу главной формы
    PERSONAL_CAB = By.XPATH, '//*[@id="root"]/div/header/nav/a/p'
    # Кнопка "Конструктор" в левом верхнем углу главной формы
    CONSTRUCTOR = By.XPATH, '//*[@id="root"]/div/header/nav/ul/li[1]/a/p'
    # Кнопка с логотипом в центре сверху главной формы
    LOGO = By.XPATH, '//*[@id="root"]/div/header/nav/div/a'
    BULKI = By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[1]/span'
    SOUSY = By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[2]/span'
    NACHINKI = By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[3]/span'
    SELECTED_SECTION = By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[@class="tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"]'

    # Форма "Авторизация"
    # Поле ввода емайла на форме "Авторизация"
    EMAIL_AUTH = By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input'
    # Поле ввода пароля на форме "Авторизация"
    PASS_AUTH = By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input'
    # Кнопка "Войти" с введенными логином (емайл) и паролем на форме "Авторизация"
    ENTER_ENTER = By.XPATH, '//*[@id="root"]/div/main/div/form/button'
    # Сообщение о неверном пароле (менее 6 символов)
    PASS_WRONG_AUTH = By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/p'


    # Форма "Регистрация"
    # Кнопка "Зарегистрироваться" в форме "Регистрация"
    ENTER_REGISTER = By.XPATH, '//*[@id="root"]/div/main/div/form/button'
    # Поле ввода имени на форме "Регистрация"
    NAME_REGISTER = By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input'
    # Поле ввода емайла на форме "Регистрация"
    EMAIL_REGISTER = By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input'
    # Поле ввода пароля на форме "Регистрация"
    PASS_REGISTER = By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/div/input'
    # Сообщение о неверном пароле (менее 6 символов)
    PASS_WRONG_REGISTER = By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/p'
    # синее слово со ссылкой "Войти"
    BLUE_ENTER = By.XPATH, '//*[@id="root"]/div/main/div/div/p/a'

    # Форма восстановления забытого пароля
    # синее слово со ссылкой "Войти" = BLUE_ENTER
    # FORGOT_PASS_ENTER = By.XPATH, '//*[@id="root"]/div/main/div/div/p/a'


    # Форма "Личный кабинет"
    # кнопка "Выход"
    EXIT_PERSONAL_CAB = By.XPATH, '//*[@id="root"]/div/main/div/nav/ul/li[3]/button'



