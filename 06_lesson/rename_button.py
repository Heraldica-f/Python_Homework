from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(5)

# Перейти на сайт http://uitestingplayground.com/textinput
driver.get('http://uitestingplayground.com/textinput')

# Указать в поле ввода текст SkyPro
field = driver.find_element(By.CSS_SELECTOR, '#newButtonName')
field.send_keys('SkyPro')

# Нажать на синюю кнопку
driver.find_element(By.CSS_SELECTOR, '#updatingButton').click()

# Получить текст кнопки и вывести в консоль ("SkyPro")
txt = driver.find_element(By.CSS_SELECTOR, '#updatingButton').text
print(txt)

driver.quit()