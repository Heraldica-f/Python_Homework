from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

#Открыть браузер FireFox
driver.get('https://www.firefox.com/')
sleep(2)

#Перейти на страницу http://the-internet.herokuapp.com/login
driver.get('http://the-internet.herokuapp.com/login')
sleep(2)

#В поле username ввести значение tomsmith
username_input = driver.find_element(By.CSS_SELECTOR, 'input#username')
username_input.send_keys('tomsmith')
sleep(2)

#В поле password ввести значение SuperSecretPassword!
password_input = driver.find_element(By.CSS_SELECTOR, 'input#password')
password_input.send_keys('SuperSecretPassword!')
sleep(2)

#Нажать кнопку Login
login_button = driver.find_element(By.CSS_SELECTOR, 'button.radius')
login_button.send_keys(Keys.RETURN)
sleep(2)
#Вывести текст с зеленой плашки в консоль
flash_text = driver.find_element(By.CSS_SELECTOR, 'div#flash').text
print(flash_text)
sleep(2)

#Закрыть браузер (метод quit())
driver.quit()