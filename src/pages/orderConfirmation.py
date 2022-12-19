from src.pages.basePage import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

class OrderConfirmationPage(BasePage):

    CONFIRMATION_MESSAGE = (By.ID, 'confirmation-message')
    DOWNLOAD_PDF = (By.ID, 'downloadpdf')
    CHECKOUT_BUTTON = (By.CLASS_NAME, 'optimizedCheckout-buttonSecondary')


    def wait_for_confirmation_message(self):
        self.wait_element_present(self.CONFIRMATION_MESSAGE)
    
    def click_continue_shopping(self):    
        self.wait_for_element_clickable(self.CHECKOUT_BUTTON).click()

    def click_download_pdf(self):
        self.wait_for_element_clickable(self.DOWNLOAD_PDF).click()

    def download_exists(self, driver, filename):
        time.sleep(20)
        assert True == driver.execute_script('browserstack_executor: {"action": "fileExists", "arguments": {"fileName": "'+ filename +'"}}')
    
    