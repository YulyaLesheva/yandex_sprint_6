import pytest

from pages.main_page import MainPage
from pages.order_page import OrderPage
from data.constants import FAQ


@pytest.mark.usefixture('driver')
class TestMainPage:
    @pytest.mark.parametrize("index, expected_question, expected_answer", FAQ)
    def test_important_questions_drop_down(self, driver, index, expected_question, expected_answer):

        main_page = MainPage(driver)
        main_page.scroll_to(main_page.important_QA)

        answer = main_page.dropdown_base_answers.format(index)
        question = main_page.dropdown_base_questions.format(index)

        main_page.click(question)
        assert main_page.get_text(question) == expected_question, "Question ERROR"
        assert main_page.get_text(answer) == expected_answer, "Answer ERROR"

    def test_order_button(self, driver):

        main_page = MainPage(driver)
        order_button = main_page.order_button

        main_page.scroll_to(order_button)
        main_page.click(order_button)

        assert OrderPage(driver).validate_is_present()
