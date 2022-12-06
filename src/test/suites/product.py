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
def test_apple_filter(driver, base_url):
    driver.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name":"Apple_Filter_Test"}}')
    login = LoginPage(driver)
    login.open_base_url(base_url)
    login.sign_in("fav_user","testingisfun99")
    home = HomePage(driver)
    home.filter_by_element()
    time.sleep(5)
    count = home.get_count_of_products()
    driver.execute_script('browserstack_executor: {"action": "annotate", "arguments": {"data":"'+ str(count) +'", "level": "<info/warn/debug/error>"}}')
    if count == 9:
        driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed","reason": "Test Passed Successfully"}}')
    else:
        driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed","reason": "Filter Not Successful"}}')

@pytest.mark.nondestructive
def test_price_filter(driver, base_url):
    driver.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name":"Price_Filter_Test"}}')
    login = LoginPage(driver)
    login.open_base_url(base_url)
    login.sign_in("fav_user","testingisfun99")
    home = HomePage(driver)
    home.select_lowest_price_filter()
    time.sleep(5)
    if home.confirm_element_name() == 'Pixel 2':
        driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed","reason": "Test Passed Successfully"}}')
    else:
        driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed","reason": "Filter Not Successful"}}')
