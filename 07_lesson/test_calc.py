from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Calculator import Calculator

def test_calc():

    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    calc_page = Calculator(browser)
    calc_page.open()
    calc_page.delay_field('45')
    calc_page.buttons_pushing('7')
    calc_page.buttons_pushing('+')
    calc_page.buttons_pushing('8')
    calc_page.buttons_pushing('=')

    WebDriverWait(browser, 45).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, 'screen'), '15')
    )

    calc_page.checking_the_result()

    browser.quit()