import pytest
from selenium import webdriver


@pytest.fixture
def chrome_driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def firefox_driver():
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()
