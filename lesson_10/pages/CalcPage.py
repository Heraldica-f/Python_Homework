import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalcPage:
    
    def __init__(self, browser: str):
        self._driver = browser
        self._wait = WebDriverWait(self._driver, 10)

    @allure.step("Открыть страницу калькулятора")
    def open(self) -> None:
        """
        Открывает страницу с калькулятором, устанавливает неявное ожидание и разворачивает окно на весь экран.
        """
        self._driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    @allure.step("Очистить строку задержки и вписать свое значение: {delay}")
    def delay_field(self, delay: str) -> None:
        """
        Очищает поле ввода задержки и устанавливает указанное значение.
        """
        delay_field = self._driver.find_element(By.CSS_SELECTOR, '#delay')
        delay_field.clear()
        delay_field.send_keys(delay)

    @allure.step("Нажать кнопку на калькуляторе {symbol}")
    def buttons_pushing(self, symbol: str) -> None:
        """
        Прожимает кнопки калькулятора по указанным значениям symbol(str)
        """
        button = self._wait.until(
                EC.element_to_be_clickable((By.XPATH, f'//span[text()="{symbol}"]'))
                )
        button.click()
    
    @allure.step("Проверка результата")
    def checking_the_result(self) -> str:
        """
        Сверяет полученный результат с ожидаемым значением
        """
        answer = self._driver.find_element(By.CLASS_NAME, 'screen').text
        assert answer == '15'