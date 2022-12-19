from src.pages.basePage import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class OrdersPage(BasePage):

    ORDER_ITEM = (By.CLASS_NAME, 'order')
    
    def verify_orders_placed(self):
        self.wait_element_present(self.ORDER_ITEM)
        try:
            self.find_element(self.ORDER_ITEM)
            return True
        except NoSuchElementException:
            return False
       
            