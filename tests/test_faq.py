from pages.main_page import MainPage
import pytest
import allure
from test_data import faq_indexes

class TestFaq:

    @allure.title('Проверка открытия ответов на часто задаваемые вопросы') 
    @allure.description('Нажимаем на часто задаваемый вопрос и проверяем отображение элемента ' \
    'с ответом (параметризованный тест, проверяем все ответы на вопросы)')
    @pytest.mark.parametrize("item_num", faq_indexes)
    def test_get_faq_answer(self, driver, item_num):
        main_page = MainPage(driver)
        main_page.click_faq_item(item_num)
        assert main_page.is_faq_answer_visible(item_num)

    @allure.title('Проверка того, что открывается только один элемент с ответом на вопрос') 
    @allure.description('Нажимаем на часто задаваемый вопрос и проверяем отображение элемента ' \
    'с ответом (параметризованный тест, проверяем все ответы на вопросы)')
    @pytest.mark.parametrize("item_num", faq_indexes)
    def test_get_faq_answer_single_visibility(self, driver, item_num):
        main_page = MainPage(driver)
        main_page.click_faq_item(item_num)
        assert main_page.is_only_faq_answer_visible(item_num)