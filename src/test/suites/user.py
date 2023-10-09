from browserstack.local import Local
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
from src.pages.loginPage import LoginPage 
from src.pages.orders import OrdersPage
from src.pages.homePage import HomePage
import os

@pytest.mark.nondestructive
def test_existing_orders(driver, base_url):
    login = LoginPage(driver)
    login.open_base_url(base_url)
    login.sign_in("existing_orders_user","testingisfun99")
    home = HomePage(driver)
    home.navigate_to_orders()
    order_confirm = OrdersPage(driver)
    status = order_confirm.verify_orders_placed()


@pytest.mark.nondestructive
def test_no_image(driver, base_url):
    login = LoginPage(driver)
    login.open_base_url(base_url)
    login.sign_in("image_not_loading_user","testingisfun99")
    home = HomePage(driver)

            
            