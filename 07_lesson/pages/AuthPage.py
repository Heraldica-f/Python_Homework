from selenium.webdriver.common.by import By

class AuthPage:

    def __init__(self, browser):
        self._driver = browser
        self._driver.get('https://www.saucedemo.com/')
        self._driver.implicitly_wait(10)
        self._driver.maximize_window()

    def login_input(self, user_name):
        username = self._driver.find_element(By.ID, 'user-name')
        username.send_keys(user_name)

    def password_input(self, password):
        pass_word = self._driver.find_element(By.ID, 'password')
        pass_word.send_keys(password)

    def push_login_button(self):
        push = self._driver.find_element(By.ID, 'login-button')
        push.click()