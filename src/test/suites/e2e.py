from src.pages.loginPage import LoginPage
from dotenv import load_dotenv
import os

load_dotenv()


#@pytest.mark.nondestructive
def test_e2e(driver, base_url="https://bstackdemo.com/"):
    #staging = os.environ.get("LOCAL") 
    base_url="https://bstackdemo.com/"
    login = LoginPage(driver)
    