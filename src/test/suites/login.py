from browserstack.local import Local
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
import time

def test_example(selenium):
    # @ansel Read the below baseURL from the JSON file so that we can use this for local as well. 
    selenium.get('https://bstackdemo.com/')
    selenium.find_element(By.ID, "signin").click()
    time.sleep(3)
    loginText = selenium.find_element(By.ID, "login-btn").text

    if loginText == "LOG IN":
        selenium.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed","reason": "Test Passed Successfully"}}')
    else:
        selenium.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed","reason": "Login Page not navigated"}}')
