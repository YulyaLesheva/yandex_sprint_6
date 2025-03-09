import pytest
import allure
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

    @allure.feature("Order Page")
    @allure.story("Fill Personal Data")
    @allure.title("Test filling personal data form")
    def test_fill_personal_data(self, driver, user):
        order_page = OrderPage(driver)

        with allure.step("Fill personal data form"):
            self.__fill_personal_data(order_page, user)

        with allure.step("Verify that rent details section is present"):
            assert order_page.is_element_present(order_page.about_rent_header)

    @allure.feature("Order Page")
    @allure.story("Fill Rent Data")
    @allure.title("Test filling rent data form")
    def test_fill_rent_data(self, driver, user):
        order_page = OrderPage(driver)

        with allure.step("Fill personal data form"):
            self.__fill_personal_data(order_page, user)

        with allure.step("Fill rent data form"):
            self.__fill_rent_data(order_page, user)

        with allure.step("Verify that confirm order section is present"):
            assert order_page.is_element_present(order_page.confirm_order_header)

    @allure.feature("Order Page")
    @allure.story("Confirm Order")
    @allure.title("Test confirming an order")
    def test_confirm_order(self, driver, user):
        order_page = OrderPage(driver)

        with allure.step("Fill personal data form"):
            self.__fill_personal_data(order_page, user)

        with allure.step("Fill rent data form"):
            self.__fill_rent_data(order_page, user)

        with allure.step("Click on accept order button"):
            order_page.click(order_page.accept_order_btn)

        with allure.step("Verify that success order header is present"):
            assert order_page.is_element_present(order_page.successes_order_header)

    @staticmethod
    @allure.step("Fill personal data form and proceed")
    def __fill_personal_data(order_page, user: User):
        order_page.fill_personal_data_form(user)
        order_page.click(order_page.continue_btn)

    @staticmethod
    @allure.step("Fill rent data form and proceed")
    def __fill_rent_data(order_page, user: User):
        order_page.fill_rent_data_form(user)
        order_page.click(order_page.order_btn)
