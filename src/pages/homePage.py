from src.pages.basePage import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):

    SIGNED_IN_USER = (By.CLASS_NAME, 'username')
    ITEM_1 = (By.CSS_SELECTOR, '[id="1"] .shelf-item__buy-btn')
    ITEM_2 = (By.CSS_SELECTOR, '[id="2"] .shelf-item__buy-btn')
    CLOSE_BTN = (By.CLASS_NAME, 'float-cart__close-btn')
    BUY_BTN=(By.CLASS_NAME, 'buy-btn')
    APPLE_FILTER = (By.CSS_SELECTOR,'input[value="Apple"] + span')
    SHELF_ITEMS = (By.CLASS_NAME, 'shelf-item')


    def signed_in_user(self):
        return self.wait_element_present(self.SIGNED_IN_USER).text

    def add_elements_to_cart(self):
        self.wait_for_element_clickable(self.ITEM_1).click()
        self.wait_for_element_clickable(self.CLOSE_BTN).click()
        self.wait_element_present(self.ITEM_2).click()

    def click_buy(self):
        self.wait_for_element_clickable(self.BUY_BTN).click()

    def filter_by_element(self):
        self.wait_for_element_clickable(self.APPLE_FILTER).click()
    
    def get_count_of_products(self):
        return len(self.find_elements(self.SHELF_ITEMS))
    
    


    