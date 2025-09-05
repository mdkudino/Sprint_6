from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import allure

# Страница с формой заказа - данные пользователя
class OrderFormPage(BasePage):
    
    first_name_input = [By.XPATH, ".//input[@placeholder='* Имя']"] # Поле Имя
    last_name_input = [By.XPATH, ".//input[@placeholder='* Фамилия']"] # Поле Фамилия
    address_input = [By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']"] # Поле с адресом
    metro_station_input = [By.XPATH, ".//input[@placeholder='* Станция метро']"] # Поле со станцией метро
    metro_options_container = [By.XPATH, ".//div[contains(@class, 'select-search__select')]"] # Выпадающий список со станциями метро
    phone_input = [By.XPATH, ".//input[contains(@placeholder, 'Телефон')]"] # Поле Телефон
    next_button = [By.XPATH, ".//button[text()='Далее']"] # Кнопка Далее

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Заполняем поле Имя')
    def set_first_name(self, first_name):
        super().fill_input(self.first_name_input, first_name)

    @allure.step('Заполняем поле Фамилия')
    def set_last_name(self, last_name):
        super().fill_input(self.last_name_input, last_name)
   
    @allure.step('Заполняем поле Имя')
    def set_address(self, address):
        super().fill_input(self.address_input, address)
    
    @allure.step('Заполняем поле Номер телефона')
    def set_phone_number(self, phone_number):
        super().fill_input(self.phone_input, phone_number)

    @allure.step('Заполняем поле Станция метро')
    def set_metro_station(self, metro_station):
        super().fill_input(self.metro_station_input, metro_station)
        super().wait_for_element_visible(self.metro_options_container)
        item_locator = [By.XPATH, f".//li[contains(text(), {metro_station})]"]
        super().wait_and_click_element(item_locator)
    
    @allure.step('Ждем загрузки страницы')
    def wait_for_load_order_page(self):
        url_part = 'order'
        super().wait_for_url_load(url_part)

    @allure.step('Заполняем форму заказа - вводим данные пользователя и переходим далее')
    def fill_order_form(self, name, surname, address, metro_station, phone_number):
        self.set_first_name(name)
        self.set_last_name(surname)
        self.set_address(address)
        self.set_metro_station(metro_station)
        self.set_phone_number(phone_number)
        super().scroll_and_click_element(self.next_button)
   