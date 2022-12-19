from src.pages.basePage import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):

    SIGN_IN = (By.ID, 'signin')
    USERNAME_FIELD = (By.CSS_SELECTOR, '#username input')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '#password input')
    LOGIN_BTN=(By.ID, 'login-btn')
    

    def sign_in(self, username, password):
        self.wait_for_element_clickable(self.SIGN_IN).click()
        self.wait_element_present(self.USERNAME_FIELD).send_keys(username+"\n")
        self.wait_element_present(self.PASSWORD_FIELD).send_keys(password+"\n")
        self.wait_for_element_clickable(self.LOGIN_BTN).click()
    
    def signed_in_user(self):
        return self.wait_element_present(self.SIGNED_IN_USER).text
        