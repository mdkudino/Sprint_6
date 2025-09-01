from selenium import webdriver
from pages.main_page import MainPage
from pages.order_form_page import OrderFormPage
from pages.rent_form_page import RentFormPage
from pages.confirm_order_page import ConfirmOrderPage
from pages.order_info_page import OrderInfoPage
from pages.track_order_page import TrackOrderPage
import pytest
import allure

class TestOrder:

    driver = None
    main_url = "https://qa-scooter.praktikum-services.ru/"

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @allure.title('Проверка позитивного сценария заказа') 
    @allure.description('Нажимаем кнопку Заказать (сверху или снизу - параметр), ' \
    'вводим все данные пользователя и заказа, подтверждаем заказ, проверяем, что открылась страница с отслеживанием заказа. '
    'Данные задаются через параметры теста')
    @pytest.mark.parametrize(
        'order_button_id, ' \
        'first_name, ' \
        'last_name, ' \
        'address, ' \
        'metro_station, ' \
        'phone_number, ' \
        'date, ' \
        'rent_period, ' \
        'color, ' \
        'comment',
        [
            [0, 'Мария', 'Петрова', 'ул. Ленина, д.13', "Черкизовская", "+79321233254", "10.10.2025", "двое суток", 0, "Test"],
            [1, 'Светлана', 'Иванова', 'пл. Свободы, д.32', "Сокольники", "+79105746381", "23.09.2025", "сутки", 1, ""],
        ]
    )
    def test_order(self, 
                   order_button_id,
                   first_name,
                   last_name, 
                   address,
                   metro_station,
                   phone_number,
                   date,
                   rent_period,
                   color, 
                   comment):
        
        self.driver.get(self.main_url)
        main_page = MainPage(self.driver)
        order_page = OrderFormPage(self.driver)
        rent_page = RentFormPage(self.driver)
        confirm_order_page = ConfirmOrderPage(self.driver)
        order_info_page = OrderInfoPage(self.driver)
        
        if order_button_id == 0:
            main_page.make_order_top_button()
        else:
            main_page.make_order_bottom_button()
        
        order_page.wait_for_load_order_page()
        order_page.fill_order_form(first_name, last_name, address, metro_station, phone_number)
       
        rent_page.wait_for_load_page()
        rent_page.fill_order_form(date, rent_period, color, comment)
        
        confirm_order_page.wait_for_load_confirm_page()
        confirm_order_page.confirm_order()
        
        order_info_page.wait_for_load_info_page()

        assert order_info_page.is_page_visible() == True

    @allure.title('Проверка перехода на главную страницу при нажатии на логотип Самокат') 
    @allure.description('Нажимаем кнопку Заказать, ' \
    'вводим все данные пользователя и заказа, подтверждаем заказ, нажимаем на логотип Самокат и проверяем, ' \
    'что открылась главная страница.')
    @pytest.mark.parametrize(
        'order_button_id, ' \
        'first_name, ' \
        'last_name, ' \
        'address, ' \
        'metro_station, ' \
        'phone_number, ' \
        'date, ' \
        'rent_period, ' \
        'color, ' \
        'comment',
        [
            [0, 'Мария', 'Петрова', 'ул. Ленина, д.13', "Черкизовская", "+79321233254", "10.10.2025", "двое суток", 0, "Test"],
        ]
    )
    def test_main_page_link(self, 
                            order_button_id,
                            first_name,
                            last_name, 
                            address,
                            metro_station,
                            phone_number,
                            date,
                            rent_period,
                            color, 
                            comment):
        
        self.driver.get(self.main_url)
        main_page = MainPage(self.driver)
        order_page = OrderFormPage(self.driver)
        rent_page = RentFormPage(self.driver)
        confirm_order_page = ConfirmOrderPage(self.driver)
        order_info_page = OrderInfoPage(self.driver)
        track_order_page = TrackOrderPage(self.driver)
        
        if order_button_id == 0:
            main_page.make_order_top_button()
        else:
            main_page.make_order_bottom_button()
        
        order_page.wait_for_load_order_page()
        order_page.fill_order_form(first_name, last_name, address, metro_station, phone_number)
       
        rent_page.wait_for_load_page()
        rent_page.fill_order_form(date, rent_period, color, comment)
        
        confirm_order_page.wait_for_load_confirm_page()
        confirm_order_page.confirm_order()
        
        order_info_page.wait_for_load_info_page()
        order_info_page.see_order_status()

        track_order_page.wait_for_load_page()
        track_order_page.go_to_main_page()

        main_page.wait_for_load_page()
        assert "Привезём его прямо к вашей двери" in main_page.get_header_text()

    @allure.title('Проверка перехода на Яндекс Дзен при нажатии логотипа Яндекс') 
    @allure.description('Нажимаем кнопку Заказать, ' \
    'вводим все данные пользователя и заказа, подтверждаем заказ, нажимаем на логотип Яндекс и проверяем, ' \
    'что открылась страница Яндекс Дзен.')
    @pytest.mark.parametrize(
        'order_button_id, ' \
        'first_name, ' \
        'last_name, ' \
        'address, ' \
        'metro_station, ' \
        'phone_number, ' \
        'date, ' \
        'rent_period, ' \
        'color, ' \
        'comment',
        [
            [0, 'Мария', 'Петрова', 'ул. Ленина, д.13', "Черкизовская", "+79321233254", "10.10.2025", "двое суток", 0, "Test"],
        ]
    )
    def test_yandex_link(   self, 
                            order_button_id,
                            first_name,
                            last_name, 
                            address,
                            metro_station,
                            phone_number,
                            date,
                            rent_period,
                            color, 
                            comment):
        
        self.driver.get(self.main_url)
        main_page = MainPage(self.driver)
        order_page = OrderFormPage(self.driver)
        rent_page = RentFormPage(self.driver)
        confirm_order_page = ConfirmOrderPage(self.driver)
        order_info_page = OrderInfoPage(self.driver)
        track_order_page = TrackOrderPage(self.driver)
        
        if order_button_id == 0:
            main_page.make_order_top_button()
        else:
            main_page.make_order_bottom_button()
        
        order_page.wait_for_load_order_page()
        order_page.fill_order_form(first_name, last_name, address, metro_station, phone_number)
       
        rent_page.wait_for_load_page()
        rent_page.fill_order_form(date, rent_period, color, comment)
        
        confirm_order_page.wait_for_load_confirm_page()
        confirm_order_page.confirm_order()
        
        order_info_page.wait_for_load_info_page()
        order_info_page.see_order_status()

        track_order_page.wait_for_load_page()
        track_order_page.go_to_dzen()

        assert "dzen.ru" in self.driver.current_url


    @classmethod
    def teardown_class(cls):
        cls.driver.quit() 