import pytest
from selenium import webdriver

@pytest.fixture(scope='function')
def setWebdriver(session_capabilities):
    remote_url = "https://hub.browserstack.com/wd/hub"

    driver = webdriver.Remote(
        command_executor=remote_url,
        desired_capabilities=session_capabilities
    )

    yield driver
    driver.quit()
