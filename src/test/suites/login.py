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

@pytest.mark.nondestructive
def test_example(driver, base_url):
    driver.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name":"Login_test"}}')
    login = LoginPage(driver, base_url)
    login.open_base_url()
    login.sign_in("fav_user","testingisfun99")
    home = HomePage(driver, base_url)
    username = home.signed_in_user()
    if username == "fav_user":
        driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed","reason": "Test Passed Successfully"}}')
    else:
        driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed","reason": "Username not found. Login Failed"}}')
