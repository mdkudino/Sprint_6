from pages.main_page import MainPage
import pytest
import allure

class TestFaq:

    @allure.title('Проверка открытия ответов на часто задаваемые вопросы') 
    @allure.description('Нажимаем на часто задаваемый вопрос и проверяем отображение элемента ' \
    'с ответом (параметризованный тест, проверяем все ответы на вопросы)')
    @pytest.mark.parametrize("item_num", [0, 1, 2, 3, 4, 5, 6, 7])
    def test_get_faq_answer(self, driver, item_num):
        main_page = MainPage(driver)
        main_page.click_faq_item(item_num)

        assert main_page.is_faq_answer_visible(item_num)

    @allure.title('Проверка того, что открывается только один элемент с ответом на вопрос') 
    @allure.description('Нажимаем на часто задаваемый вопрос и проверяем отображение элемента ' \
    'с ответом (параметризованный тест, проверяем все ответы на вопросы)')
    @pytest.mark.parametrize("item_num", [0, 1, 2, 3, 4, 5, 6, 7])
    def test_get_faq_answer_single_visibility(self, driver, item_num):
        main_page = MainPage(driver)
        main_page.click_faq_item(item_num)
        num_items = 8
        visible_list = [main_page.is_faq_answer_visible(i) for i in range(num_items) if i != item_num]
        assert visible_list == [False] * (num_items - 1)