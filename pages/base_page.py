from abc import abstractmethod

from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    # Header
    header_order_btn = "//div[contains(@class, 'Header_Nav')]//button[text()='Заказать']"
    scooter_logo = "//a[contains(@class, 'Header_LogoScooter')]"
    yandex_logo = "//a[contains(@class, 'Header_LogoYandex')]"

    def __init__(self, driver: WebDriver):
        self.driver = driver
        driver.get(self.address)

    @property
    @abstractmethod
    def address(self) -> str:
        ...

    def get_text(self, locator: str, timeout=10) -> str:

        element = WebDriverWait(self.driver, timeout).until(
            expected_conditions.presence_of_element_located((By.XPATH, locator))
        )

        WebDriverWait(self.driver, timeout).until(
            lambda d: element.text.strip() != ""
        )

        return element.text

    def scroll_to(self, locator: str, timeout=10) -> None:
        element_scroll_to = WebDriverWait(self.driver, timeout).until(
            expected_conditions.presence_of_element_located((By.XPATH, locator))
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});",
            element_scroll_to
        )

        WebDriverWait(self.driver, timeout).until(
            expected_conditions.visibility_of(element_scroll_to)
        )

    def click(self, locator: str) -> None:
        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, locator))
        )
        element.click()

    def wait_for_page_load(self, timeout=10) -> None:
        WebDriverWait(self.driver, timeout).until(
            lambda d: d.execute_script('return document.readyState') == 'complete'
        )

    def validate_is_present(self) -> bool:
        return self.driver.current_url == self.address

    def fill_field(self, locator: str, value: str) -> None:
        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, locator))
        )
        element.clear()
        element.send_keys(value)

    def is_element_present(self, locator: str) -> bool:
        try:
            WebDriverWait(self.driver, 10).until(
                expected_conditions.presence_of_element_located((By.XPATH, locator))
            )
            return True
        except Exception:
            return False

    def wait_for_new_tab(self, initial_tabs: list, timeout=10) -> None:
        WebDriverWait(self.driver, timeout).until(lambda d: len(d.window_handles) > len(initial_tabs))
