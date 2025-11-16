from src.pages.loginPage import LoginPage
from dotenv import load_dotenv
import os
import os

load_dotenv()


#@pytest.mark.nondestructive
def test_e2e(driver, base_url="https://bstackdemo.com/"):
    base_url = os.environ.get("CX_TEST_URL", base_url)
    page_source = driver.page_source
    print(f"Page Source Length: {len(page_source)}")
    # Assert that the page source length > 100
    assert len(page_source) > 100, "Page source length is not greater than 100!"
    
    