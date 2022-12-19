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

load_dotenv()


@pytest.mark.nondestructive
def test_e2e(driver, base_url):
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
    if os.environ['REMOTE'] == "true":
        order_confirm.click_download_pdf()
        order_confirm.download_exists(driver, 'confirmation.pdf' )
    order_confirm.click_continue_shopping()
    home.navigate_to_orders()
    orders = OrdersPage(driver)
    status = orders.verify_orders_placed()
    time.sleep(5)
    if os.environ['REMOTE'] == "true":
        driver.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name":"e2e_test"}}')
        if status:
            driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed","reason": "Test Passed Successfully"}}')
        else:
            driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed","reason": "Order Not Placed Successfully"}}')

            