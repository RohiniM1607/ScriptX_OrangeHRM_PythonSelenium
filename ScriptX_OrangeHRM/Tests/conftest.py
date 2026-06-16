import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def setup_and_teardown(request):
    driver = webdriver.Chrome()
    driver.maximize_window()

    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    driver.get(url)
    request.cls.driver = driver

    yield driver
    driver.quit()
    