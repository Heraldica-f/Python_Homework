import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OrderPage:

    def __init__(self, browser: str) -> None:
        self._driver = browser
        self.wait = WebDriverWait(browser, 10)
        self.fields = {
            'firstName': "Евгения",
            'lastName': "Кузьмина",
            'postalCode': "141255"
        }

    @allure.step("Заполнить форму для оформления заказа")
    def filling_form(self) -> None:
        """
        Посредством цикла заполняет поля информационной формы для оформления заказа 'First Name', 'Last Name', 'Zip/Postal Code'
        """
        for field, value in self.fields.items():
            self.wait.until(
                EC.presence_of_element_located((By.NAME, field))
            ).send_keys(value)

    @allure.step("Нажать на кнопку 'Continue'")
    def push_continue(self) -> None:
        """
        Нажимает на кнопку продолжения 'Continue' оформления заказа
        """
        Continue = self._driver.find_element(By.ID, 'continue')
        Continue.click()
    
    @allure.step("Получить финальную цену заказа")
    def total_price_get(self) -> str:
        """
        Получает финальную полную цену оформляемого заказа
        """
        total_price = self._driver.find_element(By.CLASS_NAME, 'summary_total_label')
        return total_price.text.split(': ')[1]
    
