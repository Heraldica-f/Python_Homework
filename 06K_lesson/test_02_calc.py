from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_calc_sum():

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    #Открыть страницу: https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html в Google Chrome
    driver.get(' https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')

    #В поле ввода по локатору #delay ввести значение 45
    delay_field = driver.find_element(By.CSS_SELECTOR, '#delay')
    delay_field.clear()
    delay_field.send_keys('45')

    #Нажать на кнопки:
    #7
    driver.find_element(By.XPATH, '//span[text()="7"]').click()
    #+
    driver.find_element(By.XPATH, '//span[text()="+"]').click()
    #8
    driver.find_element(By.XPATH, '//span[text()="8"]').click()
    #=
    driver.find_element(By.XPATH, '//span[text()="="]').click()

    ##Проверить через assert, что в окне отобразился результат 15 через 45 секунд
    WebDriverWait(driver, 45).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, 'screen'), '15')
    )

    answer = driver.find_element(By.CLASS_NAME, 'screen').text
    assert answer == '15'
    if answer == '15':
        print('Ответ: 15')

    driver.quit()

test_calc_sum()