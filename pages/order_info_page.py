from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import allure

# Всплывающее окно со статусом заказа
class OrderInfoPage:
    
    see_status_button = [By.XPATH, ".//button[text()='Посмотреть статус']"] # Кнопка Посмотреть статус
    status_info_text = [By.XPATH, ".//div[contains(@class, 'Order_Text')]"] # Текст статуса (с номером заказа)

    def __init__(self, driver):
        self.driver = driver
    
    @allure.step('Ждем загрузки окна со статусом')
    def wait_for_load_info_page(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.see_status_button))

    @allure.step('Проверяем, есть ли текст со статусом заказа в окне')
    def is_page_visible(self):
        return "Номер заказа" in self.driver.find_element(*self.status_info_text).get_attribute("innerText") and \
            "Посмотреть статус" in self.driver.find_element(*self.see_status_button).text
    
    @allure.step('Нажимаем на кнопку Посмотрет статус')
    def see_order_status(self):
        self.driver.find_element(*self.see_status_button).click()