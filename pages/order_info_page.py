from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import allure

# Всплывающее окно со статусом заказа
class OrderInfoPage(BasePage):
    
    see_status_button = [By.XPATH, ".//button[text()='Посмотреть статус']"] # Кнопка Посмотреть статус
    status_info_text = [By.XPATH, ".//div[contains(@class, 'Order_Text')]"] # Текст статуса (с номером заказа)

    def __init__(self, driver):
        super().__init__(driver)
    
    @allure.step('Ждем загрузки окна со статусом')
    def wait_for_load_info_page(self):
        super().wait_for_element_visible(self.see_status_button)

    @allure.step('Проверяем, есть ли текст со статусом заказа в окне')
    def is_page_visible(self):
        return "Номер заказа" in super().get_element(self.status_info_text).get_attribute("innerText") and \
            "Посмотреть статус" in super().get_element(self.see_status_button).text
    
    @allure.step('Нажимаем на кнопку Посмотрет статус')
    def see_order_status(self):
        super().click_element(self.see_status_button)