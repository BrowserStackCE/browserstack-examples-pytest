from browserstack.local import Local
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
from src.pages.loginPage import LoginPage
from src.pages.homePage import HomePage
import os

@pytest.mark.nondestructive
def test_apple_filter(driver, base_url):
    login = LoginPage(driver)
    login.open_base_url(base_url)
    login.sign_in("fav_user","testingisfun99")
    home = HomePage(driver)
    home.filter_by_element()
    time.sleep(5)
    count = home.get_count_of_products()


@pytest.mark.nondestructive
def test_price_filter(driver, base_url):
    login = LoginPage(driver)
    login.open_base_url(base_url)
    login.sign_in("fav_user","testingisfun99")
    home = HomePage(driver)
    home.select_lowest_price_filter()
    time.sleep(5)


