from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
waiting = WebDriverWait(driver, 15)

# Перейти на сайт https://bonigarcia.dev/selenium-webdriver-java/loading-images.html
driver.get('https://bonigarcia.dev/selenium-webdriver-java/loading-images.html')

# Дождаться загрузки всех картинок
waiting.until(
    EC.invisibility_of_element_located((By.CSS_SELECTOR, "#spinner"))
)
# Получить значение атрибута src у 3-й картинки
images = driver.find_elements(By.CSS_SELECTOR, '#image-container img')
third_image_src = images[2].get_attribute('src')

# Вывести значение в консоль
print(third_image_src)

driver.quit()