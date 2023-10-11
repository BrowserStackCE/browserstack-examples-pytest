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
def test_login(driver, base_url):
    login = LoginPage(driver)
    login.open_base_url(base_url)
    login.sign_in("fav_user","testingisfun99")
    home = HomePage(driver)
    username = home.signed_in_user()



@pytest.mark.nondestructive
def test_login_locked_user(driver, base_url="https://bstackdemo.com/"):
    login = LoginPage(driver)
    login.open_base_url(base_url)
    login.sign_in("locked_user","testingisfun99")
    text = login.wait_element_present((By.CLASS_NAME, 'api-error')).text


