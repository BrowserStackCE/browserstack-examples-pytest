from src.pages.basePage import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class OrderConfirmation(BasePage):

    ORDERS_MENU = (By.ID, 'orders')
    ORDER_ITEM = (By.CLASS_NAME, 'order')

    def click_orders(self):
        self.wait_for_element_clickable(self.ORDERS_MENU).click()
    
    def verify_orders_placed(self):
        self.wait_element_present(self.ORDER_ITEM)
        try:
            self.find_element(self.ORDER_ITEM)
            return True
        except NoSuchElementException:
            return False