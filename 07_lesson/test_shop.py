from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

from pages.AuthPage import AuthPage
from pages.MainPage import MainPage
from pages.CartPage import CartPage
from pages.OrderPage import OrderPage

def test_shop():

    browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    auth_page = AuthPage(browser)
    auth_page.login_input('standard_user')
    auth_page.password_input('secret_sauce')
    auth_page.push_login_button()

    main_page = MainPage(browser)
    main_page.add_to_cart('add-to-cart-sauce-labs-backpack')
    main_page.add_to_cart('add-to-cart-sauce-labs-bolt-t-shirt')
    main_page.add_to_cart('add-to-cart-sauce-labs-onesie')
    main_page.go_to_cart()

    cart_page = CartPage(browser)
    cart_page.push_checkout()

    order_page = OrderPage(browser)
    order_page.filling_form()
    order_page.push_continue()
    as_is = order_page.total_price_get()

    browser.quit()

    assert as_is == '$58.29'
    if as_is == '$58.29':
        return f'Итоговая сумма: {as_is}'