from time import sleep
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
#from webdriver_manager.microsoft import EdgeChromiumDriverManager #стандартный путь при стабильном соединении без проблем с настройкой хоста
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def waiting_for_the_zip_code_field_to_turn_red(driver):
    zip_element = driver.find_element(By.ID, 'zip-code')
    zip_class = zip_element.get_attribute('class')
    if "alert-danger" in zip_class:
        return True
    else:
        return False

def test_field_filling():
    
    driver_path = r'C:\Users\11995\OneDrive\Рабочий стол\Hometask\Python_Homework\msedgedriver.exe' # проблема с настройкой хоста, поэтому указала путь до вебдрайвера

    driver = webdriver.Edge(service=EdgeService(driver_path))
    #driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install())) #стандартный путь при стабильном соединении



    # открыть страницу: https://bonigarcia.dev/selenium-webdriver-java/data-types.html
    driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')

    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'input'))
    )

    # заполнить форму значениями
    first_name = driver.find_element(By.CSS_SELECTOR,'[name="first-name"]')
    first_name.send_keys('Иван')

    last_name = driver.find_element(By.CSS_SELECTOR,'[name="last-name"]')
    last_name.send_keys('Петров')

    address = driver.find_element(By.CSS_SELECTOR,'[name="address"]')
    address.send_keys('Ленина, 55-3')

    email = driver.find_element(By.CSS_SELECTOR,'[name="e-mail"]')
    email.send_keys('test@skypro.com')

    phone_number = driver.find_element(By.CSS_SELECTOR,'[name="phone"]')
    phone_number.send_keys('+7985899998787')

    city = driver.find_element(By.CSS_SELECTOR,'[name="city"]')
    city.send_keys('Москва')

    country = driver.find_element(By.CSS_SELECTOR,'[name="country"]')
    country.send_keys('Россия')

    job_position = driver.find_element(By.CSS_SELECTOR,'[name="job-position"]')
    job_position.send_keys('QA')

    company = driver.find_element(By.CSS_SELECTOR,'[name="company"]')
    company.send_keys('SkyPro')

    # нажать кнопку Submit
    driver.find_element(By.CSS_SELECTOR, 'button').click()

    WebDriverWait(driver, 20).until(waiting_for_the_zip_code_field_to_turn_red)

    zip_element = driver.find_element(By.ID, 'zip-code')
    zip_class = zip_element.get_attribute('class')
    assert 'alert-danger' in zip_class
    print('Zip-code красный!')

    success_alerts = driver.find_elements(By.CSS_SELECTOR, '.alert-success')
    if len(success_alerts) == 9:
        print('Остальные поля зеленые!')

    print('ВСЕ ТЕСТЫ ПРОЙДЕНЫ УСПЕШНО!')

    driver.quit()

test_field_filling()