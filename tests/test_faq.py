from selenium import webdriver
from pages.main_page import MainPage
import pytest
import allure

class TestFaq:

    driver = None
    main_url = "https://qa-scooter.praktikum-services.ru/"

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @allure.title('Проверка открытия ответов на часто задаваемые вопросы') 
    @allure.description('Нажимаем на часто задаваемый вопрос и проверяем отображение элемента ' \
    'с ответом (параметризованный тест, проверяем все ответы на вопросы)')
    @pytest.mark.parametrize("item_num", [0, 1, 2, 3, 4, 5, 6, 7])
    def test_get_faq_answer(self, item_num):
        self.driver.get(self.main_url)
        main_page = MainPage(self.driver)
        main_page.click_faq_item(item_num)
        for i in range(8):
            if i == item_num:
                assert main_page.is_faq_answer_visible(i) == True
            else:
                assert main_page.is_faq_answer_visible(i) == False

    @classmethod
    def teardown_class(cls):
        cls.driver.quit() 