from browserstack.local import Local
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
from src.pages.loginPage import LoginPage 
from src.pages.orderConfirmation import OrderConfirmation

@pytest.mark.nondestructive
def test_example(driver, base_url):
    driver.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name":"User_test"}}')
    login = LoginPage(driver, base_url)
    login.open_base_url()
    login.sign_in("existing_orders_user","testingisfun99")
    order_confirm = OrderConfirmation(driver, base_url)
    order_confirm.click_orders()
    status = order_confirm.verify_orders_placed()
    time.sleep(5)
    if status:
        driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed","reason": "Test Passed Successfully"}}')
    else:
        driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed","reason": "Order Not Placed Successfully"}}')