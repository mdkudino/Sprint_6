import pytest
from selenium import webdriver
from test_data import main_url


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get(main_url)
    yield driver
    driver.quit()
