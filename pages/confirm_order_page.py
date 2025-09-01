from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import allure

# Окно подтверждения заказа
class ConfirmOrderPage:
    
    confirm_order_button = [By.XPATH, ".//button[text()='Да']"] # Кнопка Да
    cancel_order_button = [By.XPATH, ".//button[text()='Нет']"] # Кнопка Нет
    confirm_order_modal = [By.XPATH, ".//div[contains(@class, 'Order_Modal')]"] # Текущее всплывающее окно (подтверждения)
    
    def __init__(self, driver):
        self.driver = driver
    
    @allure.step('Дожидаемся загрузки всплывающего окна')
    def wait_for_load_confirm_page(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.confirm_order_modal))

    @allure.step('Подтверждаем заказ - нажимаем кнопку Да')    
    def confirm_order(self):
        self.driver.find_element(*self.confirm_order_button).click()

    @allure.step('Отменяпм заказ - нажимаем кнопку Нет')
    def cancel_order(self):
        self.driver.find_element(*self.cancel_order_button).click()
   

    
   