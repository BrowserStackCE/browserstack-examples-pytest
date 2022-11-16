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

    def shipping_details(self, firstname, lastname, address, province, postCode):
        self.wait_element_present(self.FIRSTNAME).send_keys(firstname+'\n')
        self.wait_element_present(self.LASTNAME).send_keys(lastname+'\n')
        self.wait_element_present(self.ADDRESS).send_keys(address+'\n')
        self.wait_element_present(self.PROVINCE).send_keys(province+'\n')
        self.wait_element_present(self.POST_CODE).send_keys(postCode+'\n')

    def click_on_checkout(self):
        self.wait_for_element_clickable(self.CHECKOUT_SHIPPING_CONTINUE).click()
        self.wait_for_element_clickable(self.CHECKOUT_BUTTON).click()

    

