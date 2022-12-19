from src.pages.basePage import BasePage
from selenium.webdriver.common.by import By

class CheckoutPage(BasePage):

    FIRSTNAME = (By.ID, 'firstNameInput')
    LASTNAME = (By.ID, 'lastNameInput')
    ADDRESS = (By.ID, 'addressLine1Input')
    PROVINCE = (By.ID, 'provinceInput')
    POST_CODE= (By.ID, 'postCodeInput')
    CHECKOUT_SHIPPING_CONTINUE = (By.ID, 'checkout-shipping-continue')
    CHECKOUT_BUTTON = (By.CLASS_NAME, 'optimizedCheckout-buttonSecondary')
        
    def enterFirstName(self, firstname):    
        self.wait_element_present(self.FIRSTNAME).send_keys(firstname+'\n')
    
    def enterLastName(self, lastname):   
        self.wait_element_present(self.LASTNAME).send_keys(lastname+'\n')
    
    def enterAddressLine(self, address):   
        self.wait_element_present(self.ADDRESS).send_keys(address+'\n')
    
    def enterProvince(self, province):   
        self.wait_element_present(self.PROVINCE).send_keys(province+'\n')
    
    def enterPostCode(self, postCode):   
        self.wait_element_present(self.POST_CODE).send_keys(postCode)

    def click_on_checkout(self):
        self.wait_for_element_clickable(self.CHECKOUT_SHIPPING_CONTINUE).click()

