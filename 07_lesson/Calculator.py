from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Calculator:
    def __init__(self, browser):
        self._driver = browser
        self._wait = WebDriverWait(self._driver, 10)

    def open(self):
        self._driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    def delay_field(self, delay):
        delay_field = self._driver.find_element(By.CSS_SELECTOR, '#delay')
        delay_field.clear()
        delay_field.send_keys(delay)

    def buttons_pushing(self, symbol):
        button = self._wait.until(
                EC.element_to_be_clickable((By.XPATH, f'//span[text()="{symbol}"]'))
                )
        button.click()
    
    def checking_the_result(self):
        answer = self._driver.find_element(By.CLASS_NAME, 'screen').text
        assert answer == '15'
        if answer == '15':
            return 'Ответ: 15'