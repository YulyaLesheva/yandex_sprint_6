from selenium.webdriver.support.wait import WebDriverWait

from pages.main_page import MainPage
from pages.order_page import OrderPage
from data.constants import YANDEX


class TestHeader:

    def test_order_button(self, driver):

        main_page = MainPage(driver)
        order_button = main_page.header_order_btn

        main_page.click(order_button)

        assert OrderPage(driver).validate_is_present()

    def test_scooter_logo(self, driver):

        order_page = OrderPage(driver)
        order_page.click(order_page.scooter_logo)

        assert MainPage(driver).validate_is_present()

    def test_yandex_logo(self, driver):

        main_page = MainPage(driver)

        initial_tabs = driver.window_handles
        main_page.click(main_page.yandex_logo)

        WebDriverWait(driver, timeout=10).until(lambda d: len(d.window_handles) > len(initial_tabs))
        new_tab = [tab for tab in driver.window_handles if tab not in initial_tabs][0]

        driver.switch_to.window(new_tab)

        WebDriverWait(driver, timeout=20).until(lambda d: YANDEX in d.current_url)

        assert YANDEX in driver.current_url
