from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


#Открыть браузер Google Chrome
driver.get('https://www.google.com/')
sleep(2)

#Перейти на страницу: http://uitestingplayground.com/dynamicid
driver.get('http://uitestingplayground.com/dynamicid')
sleep(2)

#Кликнуть на синюю кнопку
push_input = driver.find_element(By.CSS_SELECTOR, 'button.btn-primary')
push_input.send_keys(Keys.RETURN)
sleep(2)

driver.quit()