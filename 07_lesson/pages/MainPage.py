from selenium.webdriver.common.by import By

class MainPage:

    def __init__(self, browser):
        self._driver = browser

    def add_to_cart(self, id):
        product = self._driver.find_element(By.ID, id)
        product.click()

    def go_to_cart(self):
       cart = self._driver.find_element(By.CLASS_NAME, 'shopping_cart_link')
       cart.click() 
