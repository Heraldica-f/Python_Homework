import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.CalcPage import CalcPage


@allure.title("Тестирование медленного калькулятора")
@allure.description("Вычисление суммы и ожидание результата для проверки")
@allure.feature("Сложение")
@allure.severity("blocker")
def test_calc():

    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    calc_page = CalcPage(browser)
    calc_page.open()
    calc_page.delay_field('45')
    calc_page.buttons_pushing('7')
    calc_page.buttons_pushing('+')
    calc_page.buttons_pushing('8')
    calc_page.buttons_pushing('=')

    with allure.step("Ожидание истечения счетчика..."):
        WebDriverWait(browser, 45).until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, 'screen'), '15')
        )

    calc_page.checking_the_result()
    
    with allure.step("Закрыть браузер"):
        browser.quit()