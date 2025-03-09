import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data.constants import FAQ


@pytest.mark.usefixture('driver')
class TestMainPage:

    @allure.feature("Main Page")
    @allure.story("FAQ Dropdown")
    @allure.title("Test FAQ dropdown questions and answers")
    @pytest.mark.parametrize("index, expected_question, expected_answer", FAQ)
    def test_important_questions_drop_down(self, driver, index, expected_question, expected_answer):
        main_page = MainPage(driver)

        with allure.step("Scroll to FAQ section"):
            main_page.scroll_to(main_page.important_QA)

        answer = main_page.dropdown_base_answers.format(index)
        question = main_page.dropdown_base_questions.format(index)

        with allure.step(f"Click on FAQ question {index}"):
            main_page.click(question)

        with allure.step("Verify that the displayed question is correct"):
            assert main_page.get_text(question) == expected_question, "Question ERROR"

        with allure.step("Verify that the displayed answer is correct"):
            assert main_page.get_text(answer) == expected_answer, "Answer ERROR"

    @allure.feature("Main Page")
    @allure.story("Order Button Navigation")
    @allure.title("Test Order Button redirects to Order Page")
    def test_order_button(self, driver):
        main_page = MainPage(driver)
        order_button = main_page.order_button

        with allure.step("Scroll to Order button"):
            main_page.scroll_to(order_button)

        with allure.step("Click on Order button"):
            main_page.click(order_button)

        with allure.step("Verify that Order Page is opened"):
            assert OrderPage(driver).validate_is_present()
