from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import allure

# Страница отслеживания заказа
class TrackOrderPage(BasePage):
    
    scooter_logo = [By.XPATH, ".//a[contains(@class, 'LogoScooter')]"] # Логотип Самокат
    yandex_logo = [By.XPATH, ".//a[contains(@class, 'LogoYandex')]"]   # Логотип Яндекс

    def __init__(self, driver):
        super().__init__(driver)
    
    @allure.step('Ждем загрузки страницы с отслеживанием заказа')
    def wait_for_load_page(self):
        url_part = "track"
        self.wait_for_url_load(url_part)

    @allure.step('Кликаем на логотип Самокат - переходим на главную страницу')
    def go_to_main_page(self):
        self.click_element(self.scooter_logo)
    
    @allure.step('Кликаем на логотип Яндекс - переходим на страницу Дзена')
    def go_to_dzen(self):
        self.click_element(self.yandex_logo)
        self.switch_to_another_tab()
        url_dzen = "dzen.ru"
        self.wait_for_url_load(url_dzen)
