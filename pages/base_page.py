from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def get_element(self, locator):
        return self.driver.find_element(*locator)
    
    def click_element(self, locator):
        self.driver.find_element(*locator).click()

    def scroll_and_click_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locator))
        element.click()

    def wait_and_click_element(self, locator):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(locator)).click()

    def wait_for_element_visible(self, locator):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locator))

    def wait_for_url_load(self, url):
         WebDriverWait(self.driver, 3).until(expected_conditions.url_contains(url))
         return self.driver.current_url

    def fill_input(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    def fill_calendar(self, locator, date):
        element = self.driver.find_element(*locator)
        element.send_keys(date)
        element.send_keys(Keys.ENTER)

    def switch_to_another_tab(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.number_of_windows_to_be(2))
        original_window = self.driver.current_window_handle
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                break