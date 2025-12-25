from selenium.webdriver.common.by import By

class CartPage:

    def __init__(self, browser):
        self._driver = browser

    def push_checkout(self):
        checkout = self._driver.find_element(By.ID, 'checkout')
        checkout.click()

    #def checking_the_content(self):
