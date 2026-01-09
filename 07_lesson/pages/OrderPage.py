from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OrderPage:

    def __init__(self, browser):
        self._driver = browser
        self.wait = WebDriverWait(browser, 10)
        self.fields = {
            'firstName': "Евгения",
            'lastName': "Кузьмина",
            'postalCode': "141255"
        }

    def filling_form(self):
        for field, value in self.fields.items():
            self.wait.until(
                EC.presence_of_element_located((By.NAME, field))
            ).send_keys(value)

    def push_continue(self):
        Continue = self._driver.find_element(By.ID, 'continue')
        Continue.click()
    
    def total_price_get(self):
        total_price = self._driver.find_element(By.CLASS_NAME, 'summary_total_label')
        return total_price.text.split(': ')[1]
    
