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
    selenium.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name":"Product_test"}}')
    selenium.get(base_url)
    WebDriverWait(selenium, 20).until(EC.element_to_be_clickable((By.ID, 'signin')))
    selenium.find_element(By.ID, "signin").click()
    #Entering the username
    WebDriverWait(selenium, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#username input')))
    username = selenium.find_element(By.CSS_SELECTOR, "#username input")
    username.send_keys("fav_user\n")
    #Entering the password
    WebDriverWait(selenium, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#password input')))
    password = selenium.find_element(By.CSS_SELECTOR, "#password input")
    password.send_keys("testingisfun99\n")
    #Clicking on Login
    WebDriverWait(selenium, 20).until(EC.element_to_be_clickable((By.ID, 'login-btn')))
    selenium.find_element(By.ID, "login-btn").click()
    #Filter by vendor "Apple"
    # WebDriverWait(selenium, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, 'shelf-item__title')))
    # count = len(selenium.find_elements(By.CLASS_NAME, 'shelf-item__title'))
    WebDriverWait(selenium, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[value="Apple"] + span')))
    selenium.find_element(By.CSS_SELECTOR,'input[value="Apple"] + span').click()
    WebDriverWait(selenium, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, 'shelf-item')))
    count = len(selenium.find_elements(By.CLASS_NAME, 'shelf-item'))
    if count == 9:
        selenium.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed","reason": "Test Passed Successfully"}}')
    else:
        selenium.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed","reason": "Filter Not Successful"}}')
