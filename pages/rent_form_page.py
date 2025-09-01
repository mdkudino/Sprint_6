from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import allure

# Окно с формой аренды
class RentFormPage:
    
    rent_date = [By.XPATH, ".//input[@placeholder='* Когда привезти самокат']"] # Поле Дата аренды
    rent_period = [By.XPATH, ".//*[contains(@class, 'Dropdown-control')]"]      # Поле Длительность аренды
    rent_menu = [By.XPATH, ".//*[contains(@class, 'Dropdown-menu')]"]           # Выпадающее меню с длительностью аренды
    black_color_check_box = [By.ID, 'black']                                    # Чек-бокс с черным цветом
    grey_color_check_box = [By.ID, 'grey']                                      # Чек-бокс с серым цветом
    comment_form = [By.XPATH, ".//input[@placeholder='Комментарий для курьера']"]   # Поле с комментарием для курьера
    confirm_order_button = [By.XPATH, ".//button[(text()='Заказать') and contains(@class, 'Button_Middle')]"] # Кнопка подтверждения заказа
    
    def __init__(self, driver):
        self.driver = driver
    
    def set_rent_date(self, date):
        calendar = self.driver.find_element(*self.rent_date)
        calendar.send_keys(date)
        calendar.send_keys(Keys.ENTER)

    def set_period(self, period):
        self.driver.find_element(*self.rent_period).click()
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.rent_menu))
        option =  WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable([By.XPATH, f".//div[text()='{period}']"]))
        option.click()

    def set_color(self, color_option):
        if color_option == 0:
            self.driver.find_element(*self.black_color_check_box).click()
        elif color_option == 1:
            self.driver.find_element(*self.grey_color_check_box).click()

    def set_comment(self, comment):
        self.driver.find_element(*self.comment_form).send_keys(comment)
    
    @allure.step('Дожидаемся загрузки страницы (окна) с параметрами аренды')
    def wait_for_load_page(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.rent_date))

    @allure.step('Заполняем данные с параметрами аренды')
    def fill_order_form(self, date, period, color_option, comment):
        self.set_rent_date(date)
        self.set_period(period)
        self.set_color(color_option)
        self.set_comment(comment)

        button = self.driver.find_element(*self.confirm_order_button)
        self.driver.execute_script("arguments[0].scrollIntoView();", button)
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.confirm_order_button))
        button.click()