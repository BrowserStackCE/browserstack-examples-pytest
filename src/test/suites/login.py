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
    if os.environ['REMOTE'] == "true":
        driver.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name":"Login_Test"}}')
        if username == "fav_user":
            driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed","reason": "Test Passed Successfully"}}')
        else:
            driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed","reason": "Username not found. Login Failed"}}')


@pytest.mark.nondestructive
def test_login_locked_user(driver, base_url):
    login = LoginPage(driver)
    login.open_base_url(base_url)
    login.sign_in("locked_user","testingisfun99")
    text = login.wait_element_present((By.CLASS_NAME, 'api-error')).text
    if os.environ['REMOTE'] == "true":
        driver.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name":"Login_Test_Locked_User"}}')
        if text == "Your account has been locked.":
            driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed","reason": "Test Passed Successfully"}}')
        else:
            driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed","reason": "Locked User Test Failed"}}')

