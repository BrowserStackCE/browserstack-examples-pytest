from browserstack.local import Local
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
import os

@pytest.mark.nondestructive
def test_example(driver, base_url="https://bstackdemo.com/"):
    driver.get(base_url)

    # locating product on webpage and getting name of the product
    productText = driver.find_element(By.XPATH, '//*[@id="1"]/p').text

    # clicking the 'Add to cart' button
    driver.find_element(By.XPATH, '//*[@id="1"]/div[4]').click()

    # waiting until the Cart pane has been displayed on the webpage
    driver.find_element(By.CLASS_NAME, 'float-cart__content')

    # locating product in cart and getting name of the product in cart
    productCartText = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[2]/div[2]/div[2]/div/div[3]/p[1]').text


