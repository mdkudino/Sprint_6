from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import allure

# Окно с формой аренды
class RentFormPage(BasePage):
    
    rent_date = [By.XPATH, ".//input[@placeholder='* Когда привезти самокат']"] # Поле Дата аренды
    rent_period = [By.XPATH, ".//*[contains(@class, 'Dropdown-control')]"]      # Поле Длительность аренды
    rent_menu = [By.XPATH, ".//*[contains(@class, 'Dropdown-menu')]"]           # Выпадающее меню с длительностью аренды
    black_color_check_box = [By.ID, 'black']                                    # Чек-бокс с черным цветом
    grey_color_check_box = [By.ID, 'grey']                                      # Чек-бокс с серым цветом
    comment_form = [By.XPATH, ".//input[@placeholder='Комментарий для курьера']"]   # Поле с комментарием для курьера
    confirm_order_button = [By.XPATH, ".//button[(text()='Заказать') and contains(@class, 'Button_Middle')]"] # Кнопка подтверждения заказа
    
    def __init__(self, driver):
        super().__init__(driver)
    
    @allure.step('Заполняем поле Дата аренды')
    def set_rent_date(self, date):
        super().fill_calendar(self.rent_date, date)

    @allure.step('Выбираем период аренды')
    def set_period(self, period):
        super().click_element(self.rent_period)
        super().wait_for_element_visible(self.rent_menu)
        menu_locator = [By.XPATH, f".//div[text()='{period}']"]
        super().wait_and_click_element(menu_locator)

    @allure.step('Выбираем цвет самоката')
    def set_color(self, color_option):
        if color_option == 0:
            super().click_element(self.black_color_check_box)
        elif color_option == 1:
            super().click_element(self.grey_color_check_box)

    @allure.step('Заполняем поле Комментарий')
    def set_comment(self, comment):
        super().fill_input(self.comment_form, comment)
    
    @allure.step('Дожидаемся загрузки страницы (окна) с параметрами аренды')
    def wait_for_load_page(self):
        super().wait_for_element_visible(self.rent_date)

    @allure.step('Заполняем данные с параметрами аренды')
    def fill_order_form(self, date, period, color_option, comment):
        self.set_rent_date(date)
        self.set_period(period)
        self.set_color(color_option)
        self.set_comment(comment)
        super().scroll_and_click_element(self.confirm_order_button)
