from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

@pytest.mark.nondestructive
def test_example(selenium, base_url):
    selenium.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name":"e2e_test"}}')
    selenium.get(base_url)
    #Clicking the Sign-in button
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
    #Adding Two elements to the cart
    WebDriverWait(selenium, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[id="1"] .shelf-item__buy-btn')))
    selenium.find_element(By.CSS_SELECTOR, '[id="1"] .shelf-item__buy-btn').click()
    WebDriverWait(selenium, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, 'float-cart__close-btn')))
    selenium.find_element(By.CLASS_NAME, 'float-cart__close-btn').click()
    WebDriverWait(selenium, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[id="2"] .shelf-item__buy-btn')))
    selenium.find_element(By.CSS_SELECTOR, '[id="2"] .shelf-item__buy-btn').click()
    #Click Buy
    WebDriverWait(selenium, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, 'buy-btn')))
    selenium.find_element(By.CLASS_NAME, 'buy-btn').click()
    #Enter shipping details "first", "last", "test address", "test province" and "123456"
    WebDriverWait(selenium, 20).until(EC.element_to_be_clickable((By.ID, 'firstNameInput')))
    selenium.find_element(By.ID, 'firstNameInput').send_keys('first\n')
    selenium.find_element(By.ID, 'lastNameInput').send_keys('last\n')
    selenium.find_element(By.ID, 'addressLine1Input').send_keys('test address\n')
    selenium.find_element(By.ID, 'provinceInput').send_keys('test province\n')
    selenium.find_element(By.ID, 'postCodeInput').send_keys('123456')
    #Click on Checkout
    WebDriverWait(selenium, 20).until(EC.element_to_be_clickable((By.ID, 'checkout-shipping-continue'))) 
    selenium.find_element(By.ID, 'checkout-shipping-continue').click()
    WebDriverWait(selenium, 20).until(EC.element_to_be_clickable((By.CLASS_NAME,'optimizedCheckout-buttonSecondary'))) 
    selenium.find_element(By.CLASS_NAME, 'optimizedCheckout-buttonSecondary').click()
    #Click on "Orders" link
    WebDriverWait(selenium, 20).until(EC.element_to_be_clickable((By.ID, 'orders')))
    selenium.find_element(By.ID, 'orders').click()
    #Click should see elements in list
    time.sleep(5)
    try:
        selenium.find_element(By.CLASS_NAME,'order')
        selenium.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed","reason": "Test Passed Successfully"}}')
    except NoSuchElementException:
        selenium.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed","reason": "Order Not Placed Successfully"}}')