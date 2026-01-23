import allure
from selenium.webdriver.common.by import By

class CartPage:

    def __init__(self, browser: str) -> None:
        self._driver = browser

    @allure.step("Нажать на кнопку checkout")
    def push_checkout(self) -> None:
        """
        Нажимает на кнопку проверки 'Checkout'
        """
        checkout = self._driver.find_element(By.ID, 'checkout')
        checkout.click()
