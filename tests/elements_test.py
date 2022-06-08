from pages.elements_page import TextBoxPage, CheckBoxPage


class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_current_address, output_per_address = text_box_page.check_filled_form()
            assert full_name == output_name, "The full name doesn't match"
            assert email == output_email, "The email doesn't match"
            assert current_address == output_current_address, "The current address doesn't match"
            assert permanent_address == output_per_address, "The permanent address doesn't match"

    class TestCheckBox:

        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, "https://demoqa.com/checkbox")
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkbox = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_output_result()
            assert input_checkbox == output_result, 'checkboxes have bot been selected'
