from browserstack.local import Local
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By

@pytest.mark.nondestructive
def test_example(driver, base_url):
    driver.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name":"addToCart_test"}}')
    driver.get(base_url)

    # locating product on webpage and getting name of the product
    productText = driver.find_element(By.XPATH, '//*[@id="1"]/p').text

    # clicking the 'Add to cart' button
    driver.find_element(By.XPATH, '//*[@id="1"]/div[4]').click()

    # waiting until the Cart pane has been displayed on the webpage
    driver.find_element(By.CLASS_NAME, 'float-cart__content')

    # locating product in cart and getting name of the product in cart
    productCartText = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[2]/div[2]/div[2]/div/div[3]/p[1]').text

    # checking whether product has been added to cart by comparing product name and marking test pass or fail
    if productText == productCartText:
        driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed","reason": "Test Passed Successfully"}}')
    else:
        driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed","reason": "Product added to the cart not same as selected"}}')
