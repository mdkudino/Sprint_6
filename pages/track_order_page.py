from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import allure

# Страница отслеживания заказа
class TrackOrderPage:
    
    scooter_logo = [By.XPATH, ".//a[contains(@class, 'LogoScooter')]"] # Логотип Самокат
    yandex_logo = [By.XPATH, ".//a[contains(@class, 'LogoYandex')]"]   # Логотип Яндекс

    def __init__(self, driver):
        self.driver = driver
    
    @allure.step('Ждем загрузки страницы с отслеживанием заказа')
    def wait_for_load_page(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.url_contains("track"))

    @allure.step('Кликаем на логотип Самокат - переходим на главную страницу')
    def go_to_main_page(self):
        self.driver.find_element(*self.scooter_logo).click()
    
    @allure.step('Кликаем на логотип Яндекс - переходим на страницу Дзена')
    def go_to_dzen(self):
        self.driver.find_element(*self.yandex_logo).click()
        WebDriverWait(self.driver, 3).until(expected_conditions.number_of_windows_to_be(2))
        original_window = self.driver.current_window_handle
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                break
        WebDriverWait(self.driver, 3).until(expected_conditions.url_contains("dzen.ru"))