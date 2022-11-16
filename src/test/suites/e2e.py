from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from src.pages.loginPage import LoginPage
from src.pages.homePage import HomePage
from src.pages.checkoutPage import CheckoutPage
from src.pages.orderConfirmation import OrderConfirmation


@pytest.mark.nondestructive
def test_example(driver, base_url):
    driver.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name":"e2e_test"}}')
    login = LoginPage(driver, base_url)
    login.open_base_url()
    login.sign_in("fav_user","testingisfun99")
    home = HomePage(driver, base_url)
    home.add_elements_to_cart()
    home.click_buy()
    checkout = CheckoutPage(driver, base_url)
    checkout.shipping_details('first','last','test address','test province','123456')
    checkout.click_on_checkout()
    order_confirm = OrderConfirmation(driver, base_url)
    order_confirm.click_orders()
    status = order_confirm.verify_orders_placed()
    time.sleep(5)
    if status:
        driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed","reason": "Test Passed Successfully"}}')
    else:
        driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed","reason": "Order Not Placed Successfully"}}')