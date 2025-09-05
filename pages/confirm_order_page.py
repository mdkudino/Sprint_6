from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import allure

# Окно подтверждения заказа
class ConfirmOrderPage(BasePage):
    
    confirm_order_button = [By.XPATH, ".//button[text()='Да']"] # Кнопка Да
    cancel_order_button = [By.XPATH, ".//button[text()='Нет']"] # Кнопка Нет
    confirm_order_modal = [By.XPATH, ".//div[contains(@class, 'Order_Modal')]"] # Текущее всплывающее окно (подтверждения)
    
    def __init__(self, driver):
        super().__init__(driver)
    
    @allure.step('Дожидаемся загрузки всплывающего окна')
    def wait_for_load_confirm_page(self):
        self.wait_for_element_visible(self.confirm_order_modal)

    @allure.step('Подтверждаем заказ - нажимаем кнопку Да')    
    def confirm_order(self):
        self.click_element(self.confirm_order_button)

    @allure.step('Отменяпм заказ - нажимаем кнопку Нет')
    def cancel_order(self):
        self.click_element(self.cancel_order_button)
   

    
   