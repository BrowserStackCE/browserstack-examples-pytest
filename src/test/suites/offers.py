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
def test_offers(driver, base_url="https://bstackdemo.com/"):
    driver.get(base_url)
    driver.execute_script('navigator.geolocation.getCurrentPosition = function(success){ var position = { "coords":{"latitude":"1","longitude":"103"}}; success(position);}')
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
    

