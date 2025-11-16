import os
import pytest

@pytest.mark.usefixtures('setWebdriver')
def test_e2e(self):
    base_url = os.environ.get("CX_TEST_URL", "https://bstackdemo.com/")
    self.driver.get(base_url)
    page_source = self.driver.page_source
    print(f"Page Source Length: {len(page_source)}")
    # Assert that the page source length > 100
    assert len(page_source) > 100, "Page source length is not greater than 100!"
