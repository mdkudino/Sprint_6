import pytest
from selenium import webdriver

MAIN_URL = "https://qa-scooter.praktikum-services.ru/"

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get(MAIN_URL)
    yield driver
    driver.quit()
