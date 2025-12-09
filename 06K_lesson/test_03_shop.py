from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

    
def test_shopping():

    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.implicitly_wait(20)

    #Открыть сайт магазина
    driver.get('https://www.saucedemo.com/')

    #Авторизоваться как standard_user
    driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    driver.find_element(By.ID, 'login-button').click()

    #Добавить в корзину товары:
    #Sauce Labs Backpack
    driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()

    #Sauce Labs Bolt T-Shirt
    driver.find_element(By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt').click()

    #Sauce Labs Onesie
    driver.find_element(By.ID, 'add-to-cart-sauce-labs-onesie').click()

    #Перейти в корзину
    driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()

    #Нажать Checkout
    driver.find_element(By.ID, 'checkout').click()

    #Заполнить форму своими данными:
    #Имя
    driver.find_element(By.ID, 'first-name').send_keys('Евгения')

    #Фамилия
    driver.find_element(By.ID, 'last-name').send_keys('Кузьмина')

    #Почтовый индекс
    driver.find_element(By.ID, 'postal-code').send_keys('141255')

    #Нажать кнопку Continue
    driver.find_element(By.ID, 'continue').click()

    #Прочитать со страницы итоговую стоимость(Total)
    total_text = driver.find_element(By.CLASS_NAME, 'summary_total_label').text
    total_amount = total_text.split(': ')[1]

    #Закрыть браузер
    driver.quit()

    #Проверить, что итоговая сумма равна $58.29
    assert total_amount == '$58.29'
    if total_amount == '$58.29':
        print(f'Итоговая сумма: {total_amount}')

test_shopping()