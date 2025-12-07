from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

#Открыть браузер FireFox
driver.get('https://www.firefox.com/')
sleep(2)

#Перейти на страницу: http://the-internet.herokuapp.com/inputs
driver.get('http://the-internet.herokuapp.com/inputs')
sleep(2)
#Ввести в поле текст Sky
field_input = driver.find_element(By.CSS_SELECTOR, 'input[type="number"]')
field_input.send_keys('Sky')
sleep(2)

#Очистить это поле (метод clear())
field_input.clear()
sleep(2)

#Ввести в поле текст Pro
field_input.send_keys('Pro')
sleep(2)

#Закрыть браузер (метод quit())
driver.quit()