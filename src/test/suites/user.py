from browserstack.local import Local
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

@pytest.mark.nondestructive
def test_example(selenium, base_url):
    selenium.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name":"User_test"}}')
    selenium.get(base_url)
    WebDriverWait(selenium, 20).until(EC.element_to_be_clickable((By.ID, 'signin')))
    selenium.find_element(By.ID, "signin").click()
    #Entering the username
    WebDriverWait(selenium, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#username input')))
    username = selenium.find_element(By.CSS_SELECTOR, "#username input")
    username.send_keys("existing_orders_user\n")
    #Entering the password
    WebDriverWait(selenium, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#password input')))
    password = selenium.find_element(By.CSS_SELECTOR, "#password input")
    password.send_keys("testingisfun99\n")
    #Clicking on Login
    WebDriverWait(selenium, 20).until(EC.element_to_be_clickable((By.ID, 'login-btn')))
    selenium.find_element(By.ID, "login-btn").click()
    #Click on "Orders" link
    WebDriverWait(selenium, 20).until(EC.element_to_be_clickable((By.ID, 'orders')))
    selenium.find_element(By.ID, 'orders').click()
    #Should see elements in list
    time.sleep(5)
    try:
        selenium.find_element(By.CLASS_NAME,'order')
        selenium.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed","reason": "Test Passed Successfully"}}')
    except NoSuchElementException:
        selenium.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed","reason": "Order Not Placed Successfully"}}')