from browserstack.local import Local
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By

def test_example(selenium):
     # @ansel Read the below baseURL from the JSON file so that we can use this for local as well. 
    selenium.get('https://bstackdemo.com/')

    # locating product on webpage and getting name of the product
    productText = selenium.find_element(By.XPATH, '//*[@id="1"]/p').text

    # clicking the 'Add to cart' button
    selenium.find_element(By.XPATH, '//*[@id="1"]/div[4]').click()

    # waiting until the Cart pane has been displayed on the webpage
    selenium.find_element(By.CLASS_NAME, 'float-cart__content')

    # locating product in cart and getting name of the product in cart
    productCartText = selenium.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[2]/div[2]/div[2]/div/div[3]/p[1]').text

    # checking whether product has been added to cart by comparing product name and marking test pass or fail
    if productText == productCartText:
        selenium.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed","reason": "Test Passed Successfully"}}')
    else:
        selenium.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed","reason": "Product added to the cart not same as selected"}}')
