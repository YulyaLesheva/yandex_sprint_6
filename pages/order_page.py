from data.users import User
from pages.page import Page


class OrderPage(Page):
    address = "https://qa-scooter.praktikum-services.ru/order"
    # Placeholders
    name_placeholder = "//input[@placeholder='* Имя']"
    surname_placeholder = "//input[@placeholder='* Фамилия']"
    address_placeholder = "//input[@placeholder='* Адрес: куда привезти заказ']"
    metro_placeholder = "//div[contains(@class, 'select-search')]//input[@placeholder='* Станция метро']"
    phone_placeholder = "//input[@placeholder='* Телефон: на него позвонит курьер']"
    delivery_date_placeholder = "// input[ @ placeholder = '* Когда привезти самокат']"
    prolongation_placeholder = "//div[contains(@class,'Dropdown-placeholder') and contains(text(),'Срок аренды')]"
    comment_placeholder = "//input[@placeholder='Комментарий для курьера']"
    # Dropdowns
    metro_dropdown_list = "//li[.//div[text()='{}']]//button"
    prolongation_dropdown_list = "//div[contains(@class,'Dropdown-option') and text()='{}']"
    # Checkboxes
    colour_checkbox = "// label[contains(@class, 'Checkbox_Label__3wxSf') and contains(text(), '{}')]"
    # Headers
    about_rent_header = "// div[text() = 'Про аренду']"
    confirm_order_header = "//div[contains(text(), 'Хотите оформить заказ?')]"
    successes_order_header = "//div[contains(text(), 'Заказ оформлен')]"
    # Buttons
    continue_btn = "//button[text() = 'Далее']"
    selected_date = "//div[contains(@class, 'react-datepicker__day--selected')]"
    order_btn = "//button[contains(@class, 'Button_Middle__1CSJM') and contains(text(), 'Заказать')]"
    accept_order_btn = "//button[contains(text(), 'Да')]"
    decline_order_btn = "//button[contains(text(), 'Нет')]"

    def fill_personal_data_form(self, user: User) -> None:
        fields = {
            self.name_placeholder: user.name,
            self.surname_placeholder: user.surname,
            self.address_placeholder: user.address,
            self.phone_placeholder: user.phone
        }

        for placeholder, value in fields.items():
            self.fill_field(placeholder, value)

        self.click(self.metro_placeholder)
        self.click(self.metro_dropdown_list.format(user.metro))

    def fill_rent_data_form(self, user: User) -> None:

        self.fill_field(self.delivery_date_placeholder, user.delivery_date)
        self.click(self.selected_date)

        self.click(self.prolongation_placeholder)
        self.click(self.prolongation_dropdown_list.format(user.prolongation))
        self.click(self.colour_checkbox.format(user.colour))

        if user.comment:
            self.fill_field(self.comment_placeholder, user.comment)
