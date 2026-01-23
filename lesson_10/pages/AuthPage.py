import allure
from selenium.webdriver.common.by import By

class AuthPage:

    def __init__(self, browser: str) -> None:
        self._driver = browser
        self._driver.get('https://www.saucedemo.com/')
        self._driver.implicitly_wait(10)
        self._driver.maximize_window()
    
    @allure.step("Ввести логин: {user_name}")
    def login_input(self, user_name: str) -> None:
        """
        Вводит имя пользователя в указанное поле 'Username'
        """
        username = self._driver.find_element(By.ID, 'user-name')
        username.send_keys(user_name)

    @allure.step("Ввести пароль: {password}")
    def password_input(self, password: str) -> None:
        """
        Вводит пароль пользователя в указанное поле 'Password'
        """
        pass_word = self._driver.find_element(By.ID, 'password')
        pass_word.send_keys(password)

    @allure.step("Нажать на кнопку авторизации")
    def push_login_button(self) -> None:
        """
        Нажимает кнопку авторизации 'Login'
        """
        push = self._driver.find_element(By.ID, 'login-button')
        push.click()