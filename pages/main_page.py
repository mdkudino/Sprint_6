from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import allure

# Главная страница сервиса Самокат
class MainPage:
    cookies_button = [By.XPATH, ".//button[contains(@class, 'Cookie')]"] # Кнопка подтверждения использования куков
    top_order_button = [By.CLASS_NAME, 'Button_Button__ra12g'] # Верхняя кнопка Заказать
    bottom_order_button = [By.XPATH, ".//button[text()='Заказать' and contains(@class, 'Button_Middle')]"] # Нижняя кнопка Заказать
    faq_items = [[By.ID, 'accordion__heading-' + str(f)] for f in range(8)] # Меню часто задаваемых вопросов
    answer_faq_items = [[By.ID, 'accordion__panel-' + str(f)] for f in range(8)] # Ответы на часто задаваемые вопросы
    header_scooter = [By.XPATH, ".//div[contains(text(), 'Самокат') and contains(@class, 'Home_Header')]"] # Заглавный текст

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Кликаем на вопрос')
    def click_faq_item(self, item_num):
        faq_elem = self.driver.find_element(*self.faq_items[item_num])
        self.driver.execute_script("arguments[0].scrollIntoView();", faq_elem)
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.faq_items[item_num]))
        faq_elem.click()

    def is_faq_answer_visible(self, item_num):
        return self.driver.find_element(*self.answer_faq_items[item_num]).get_attribute('hidden') is None
    
    @allure.step('Делаем заказ по верхней кнопке')
    def make_order_top_button(self):
        try:
            self.driver.find_element(*self.cookies_button).click()
        except Exception:
            pass
        self.driver.find_element(*self.top_order_button).click()

    @allure.step('Делаем заказ по нижней кнопке')
    def make_order_bottom_button(self):
        button = self.driver.find_element(*self.bottom_order_button)
        self.driver.execute_script("arguments[0].scrollIntoView();", button)
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.bottom_order_button))
        button.click()

    @allure.step('Ждем загрузки страницы')
    def wait_for_load_page(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.header_scooter))

    def get_header_text(self):
        return self.driver.find_element(*self.header_scooter).get_attribute("innerText")
    