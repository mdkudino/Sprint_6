from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import allure

# Главная страница сервиса Самокат
class MainPage(BasePage):
    cookies_button = [By.XPATH, ".//button[contains(@class, 'Cookie')]"] # Кнопка подтверждения использования куков
    top_order_button = [By.CLASS_NAME, 'Button_Button__ra12g'] # Верхняя кнопка Заказать
    bottom_order_button = [By.XPATH, ".//button[text()='Заказать' and contains(@class, 'Button_Middle')]"] # Нижняя кнопка Заказать
    faq_items_len = 8
    faq_items = [[By.ID, 'accordion__heading-' + str(f)] for f in range(faq_items_len)] # Меню часто задаваемых вопросов
    answer_faq_items = [[By.ID, 'accordion__panel-' + str(f)] for f in range(faq_items_len)] # Ответы на часто задаваемые вопросы
    header_scooter = [By.XPATH, ".//div[contains(text(), 'Самокат') and contains(@class, 'Home_Header')]"] # Заглавный текст

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Кликаем на вопрос')
    def click_faq_item(self, item_num):
        self.scroll_and_click_element(self.faq_items[item_num])
    
    @allure.step('Проверяем отображение элемента')
    def is_faq_answer_visible(self, item_num):
        return self.get_element(self.answer_faq_items[item_num]).get_attribute('hidden') is None
    
    @allure.step('Проверяем, какие элементы из списка ответов на часто задаваемые вопросы, отображаются в данный момент')
    def get_visible_faq_elements_indexes(self):
        visible = []
        for i in range(self.faq_items_len):
            if self.is_faq_answer_visible(i):
                visible.append(i)
        return visible
    
    @allure.step('Проверяем, что только один элемент в списке ответов на часто задаваемые вопросы, видим в данный момент')
    def is_only_faq_answer_visible(self, index):
        return self.get_visible_faq_elements_indexes() == [index]
    
    @allure.step('Делаем заказ')
    def make_order(self, order_button_id):
        locator = self.top_order_button

        if order_button_id == 0:
            locator = self.top_order_button
        elif order_button_id == 1:
            locator = self.bottom_order_button
        try:
            self.click_element(self.cookies_button)
        except NoSuchElementException:
            pass
        self.scroll_and_click_element(locator)

    @allure.step('Ждем загрузки страницы')
    def wait_for_load_page(self):
        self.wait_for_element_visible(self.header_scooter)

    @allure.step('Получаем заглавный текст') 
    def get_header_text(self):
        return self.get_element(self.header_scooter).get_attribute("innerText")
    