from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from src.pages.loginPage import LoginPage
from src.pages.homePage import HomePage
from src.pages.checkoutPage import CheckoutPage
from src.pages.orderConfirmation import OrderConfirmationPage
from src.pages.orders import OrdersPage

from dotenv import load_dotenv
import os
import json

load_dotenv()


#@pytest.mark.nondestructive
def test_e2e(driver, base_url="https://bstackdemo.com/"):
    staging = os.environ.get("LOCAL") 
    if (staging=="True"):
        base_url="http://localhost:3000/"
    else:
        base_url="https://bstackdemo.com/"
    login = LoginPage(driver)
    login.open_base_url(base_url)
    login.sign_in("fav_user","testingisfun99")
    home = HomePage(driver)
    home.add_elements_to_cart()
    home.click_buy()
    checkout = CheckoutPage(driver)
    checkout.enterFirstName('firstname')
    checkout.enterLastName('lastname')
    checkout.enterAddressLine('address')
    checkout.enterProvince('state')
    checkout.enterPostCode('12345')
    checkout.click_on_checkout()
    order_confirm = OrderConfirmationPage(driver)
    order_confirm.wait_for_confirmation_message()
    order_confirm.click_continue_shopping()
    home.navigate_to_orders()
    orders = OrdersPage(driver)
    status = orders.verify_orders_placed()
    time.sleep(5)
    