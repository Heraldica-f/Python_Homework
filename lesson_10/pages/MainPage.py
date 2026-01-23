import allure
from selenium.webdriver.common.by import By

class MainPage:

    def __init__(self, browser: str) -> None:
        self._driver = browser

    @allure.step("Положить товары в корзину по id: {id}")
    def add_to_cart(self, id: str) -> None:
        """
        Отправляет указанные товары в пользовательскую корзину с помощью id товара
        """
        product = self._driver.find_element(By.ID, id)
        product.click()

    @allure.step("Перейти в корзину")
    def go_to_cart(self) -> None:
       """
       Осуществляет переход в пользовательскую корзину
       """
       cart = self._driver.find_element(By.CLASS_NAME, 'shopping_cart_link')
       cart.click() 
