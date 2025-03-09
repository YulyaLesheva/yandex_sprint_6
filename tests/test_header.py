import allure
from selenium.webdriver.support.wait import WebDriverWait
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data.constants import YANDEX


class TestHeader:

    @allure.feature("Header")
    @allure.story("Order Button Navigation")
    @allure.title("Test Order Button redirects to Order Page")
    def test_order_button(self, driver):
        main_page = MainPage(driver)
        order_button = main_page.header_order_btn

        with allure.step("Click on Order button in header"):
            main_page.click(order_button)

        with allure.step("Verify that Order Page is opened"):
            assert OrderPage(driver).validate_is_present()

    @allure.feature("Header")
    @allure.story("Scooter Logo Navigation")
    @allure.title("Test Scooter Logo redirects to Main Page")
    def test_scooter_logo(self, driver):
        order_page = OrderPage(driver)

        with allure.step("Click on Scooter logo in header"):
            order_page.click(order_page.scooter_logo)

        with allure.step("Verify that Main Page is opened"):
            assert MainPage(driver).validate_is_present()

    @allure.feature("Header")
    @allure.story("Yandex Logo Navigation")
    @allure.title("Test Yandex Logo opens Yandex site in new tab")
    def test_yandex_logo(self, driver):
        main_page = MainPage(driver)

        with allure.step("Get initial tabs"):
            initial_tabs = driver.window_handles

        with allure.step("Click on Yandex logo in header"):
            main_page.click(main_page.yandex_logo)

        with allure.step("Wait for new tab to open"):
            main_page.wait_for_new_tab(initial_tabs=initial_tabs)
            new_tab = [tab for tab in driver.window_handles if tab not in initial_tabs][0]

        with allure.step("Switch to new tab"):
            driver.switch_to.window(new_tab)

        with allure.step("Verify that new tab contains Yandex URL"):
            WebDriverWait(driver, timeout=20).until(lambda d: YANDEX in d.current_url)
            assert YANDEX in driver.current_url
