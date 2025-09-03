from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import allure

# Главная страница сервиса Самокат
class MainPage(BasePage):
    cookies_button = [By.XPATH, ".//button[contains(@class, 'Cookie')]"] # Кнопка подтверждения использования куков
    top_order_button = [By.CLASS_NAME, 'Button_Button__ra12g'] # Верхняя кнопка Заказать
    bottom_order_button = [By.XPATH, ".//button[text()='Заказать' and contains(@class, 'Button_Middle')]"] # Нижняя кнопка Заказать
    faq_items = [[By.ID, 'accordion__heading-' + str(f)] for f in range(8)] # Меню часто задаваемых вопросов
    answer_faq_items = [[By.ID, 'accordion__panel-' + str(f)] for f in range(8)] # Ответы на часто задаваемые вопросы
    header_scooter = [By.XPATH, ".//div[contains(text(), 'Самокат') and contains(@class, 'Home_Header')]"] # Заглавный текст

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Кликаем на вопрос')
    def click_faq_item(self, item_num):
        super().scroll_and_click_element(self.faq_items[item_num])
    
    @allure.step('Проверяем отображение элемента')
    def is_faq_answer_visible(self, item_num):
        return super().get_element(self.answer_faq_items[item_num]).get_attribute('hidden') is None
    
    @allure.step('Делаем заказ по верхней кнопке')
    def make_order_top_button(self):
        try:
            super().click_element(self.cookies_button)
        except NoSuchElementException:
            pass
        super().click_element(self.top_order_button)

    @allure.step('Делаем заказ по нижней кнопке')
    def make_order_bottom_button(self):
        try:
            super().click_element(self.cookies_button)
        except NoSuchElementException:
            pass
        super().scroll_and_click_element(self.bottom_order_button)

    @allure.step('Ждем загрузки страницы')
    def wait_for_load_page(self):
        super().wait_for_element_visible(self.header_scooter)

    @allure.step('Получаем заглавный текст') 
    def get_header_text(self):
        return self.get_element(self.header_scooter).get_attribute("innerText")
    