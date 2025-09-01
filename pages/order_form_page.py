from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import allure

# Страница с формой заказа - данные пользователя
class OrderFormPage:
    
    first_name_input = [By.XPATH, ".//input[@placeholder='* Имя']"] # Поле Имя
    last_name_input = [By.XPATH, ".//input[@placeholder='* Фамилия']"] # Поле Фамилия
    address_input = [By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']"] # Поле с адресом
    metro_station_input = [By.XPATH, ".//input[@placeholder='* Станция метро']"] # Поле со станцией метро
    metro_options_container = [By.XPATH, ".//div[contains(@class, 'select-search__select')]"] # Выпадающий список со станциями метро
    phone_input = [By.XPATH, ".//input[contains(@placeholder, 'Телефон')]"] # Поле Телефон
    next_button = [By.XPATH, ".//button[text()='Далее']"] # Кнопка Далее

    def __init__(self, driver):
        self.driver = driver

    def set_first_name(self, first_name):
        self.driver.find_element(*self.first_name_input).send_keys(first_name)

    def set_last_name(self, last_name):
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
   
    def set_address(self, address):
        self.driver.find_element(*self.address_input).send_keys(address)
    
    def set_phone_number(self, phone_number):
        self.driver.find_element(*self.phone_input).send_keys(phone_number)

    def set_metro_station(self, metro_station):
        self.driver.find_element(*self.metro_station_input).send_keys(metro_station)
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.metro_options_container))
        option =  WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable([By.XPATH, f".//li[contains(text(), {metro_station})]"]))
        option.click()
    
    @allure.step('Ждем загрузки страницы')
    def wait_for_load_order_page(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.url_contains('order'))

    @allure.step('Заполняем форму заказа - вводим данные пользователя и переходим далее')
    def fill_order_form(self, name, surname, address, metro_station, phone_number):
        self.set_first_name(name)
        
        self.set_last_name(surname)
        self.set_address(address)
        self.set_metro_station(metro_station)
        self.set_phone_number(phone_number)
        button = self.driver.find_element(*self.next_button)
        self.driver.execute_script("arguments[0].scrollIntoView();", button)
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.next_button))
        button.click()
   

    
   