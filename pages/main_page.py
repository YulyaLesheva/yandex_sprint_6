from selenium.webdriver.ie.webdriver import WebDriver

from tests.conftest import driver
from pages.base_page import BasePage


class MainPage(BasePage):
    address = "https://qa-scooter.praktikum-services.ru/"

    dropdown_base_questions = "//div[@id='accordion__heading-{}']"
    dropdown_base_answers = "//div[@id='accordion__panel-{}']"

    important_QA = "//div[contains(@class, 'Home_SubHeader') and text()='Вопросы о важном']"
    order_button = "//div[contains(@class, 'Home_FinishButton')]//button[text()='Заказать']"

    def __init__(self, driver: WebDriver):
        super().__init__(driver=driver)
