import pytest
from data.users import User
from pages.order_page import OrderPage


@pytest.mark.usefixtures("driver")
@pytest.mark.parametrize("user", [
    User(
        name="Иван",
        surname="Иванов",
        phone="+9001234567",
        address="г. Москва, ул. Ленина, д. 1",
        metro="Сокольники",
        delivery_date="08.05.2022",
        prolongation="сутки",
        colour="чёрный жемчуг"),
    User(
        name="Петр",
        surname="Петров",
        phone="89001234568",
        address="г. Москва, ул. Дудя, д. 2",
        metro="Черкизовская",
        delivery_date="08.05.2022",
        prolongation="пятеро суток",
        colour="серая безысходность",
        comment="Never gonna give you up."),
    ])
class TestOrderPage:

    def test_fill_personal_data(self, driver, user):

        order_page = OrderPage(driver)
        self.__fill_personal_data(order_page, user)

        assert order_page.is_element_present(order_page.about_rent_header)

    def test_fill_rent_data(self, driver, user):

        order_page = OrderPage(driver)
        self.__fill_personal_data(order_page, user)
        self.__fill_rent_data(order_page, user)

        assert order_page.is_element_present(order_page.confirm_order_header)

    def test_confirm_order(self, driver, user):

        order_page = OrderPage(driver)
        self.__fill_personal_data(order_page, user)
        self.__fill_rent_data(order_page, user)

        order_page.click(order_page.accept_order_btn)
        assert order_page.is_element_present(order_page.successes_order_header)

    @staticmethod
    def __fill_personal_data(order_page, user: User):
        order_page.fill_personal_data_form(user)
        order_page.click(order_page.continue_btn)

    @staticmethod
    def __fill_rent_data(order_page, user: User):
        order_page.fill_rent_data_form(user)
        order_page.click(order_page.order_btn)
