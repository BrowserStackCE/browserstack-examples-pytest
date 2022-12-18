from browserstack.local import Local
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import os


@pytest.mark.nondestructive
def test_example(driver, base_url):
    driver.get(base_url)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'signin')))
    driver.find_element(By.ID, "signin").click()
    #Entering the username
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#username input')))
    username = driver.find_element(By.CSS_SELECTOR, "#username input")
    username.send_keys("fav_user\n")
    #Entering the password
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#password input')))
    password = driver.find_element(By.CSS_SELECTOR, "#password input")
    password.send_keys("testingisfun99\n")
    #Clicking on Login
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'login-btn')))
    driver.find_element(By.ID, "login-btn").click()
    #Click on Offers
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'offers')))
    driver.find_element(By.ID, "offers").click()
    if os.environ['REMOTE'] == "true":
        driver.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name":"Offers_test"}}')
        try:
            driver.find_element(By.CLASS_NAME,'offer')
            driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed","reason": "Test Passed Successfully"}}')
        except NoSuchElementException:
            driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed","reason": "Offers Not Found Successfully"}}')
