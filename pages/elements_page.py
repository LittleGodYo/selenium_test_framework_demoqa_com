import random

from generator.generator import generated_person
from pages.base_page import BasePage
from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonPageLocators


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address
        self.is_visible('css', self.locators.FULL_NAME).send_keys(full_name)
        self.is_visible('css', self.locators.EMAIL).send_keys(email)
        self.is_visible('css', self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.is_visible('css', self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        self.is_visible('css', self.locators.SUBMIT).click()
        return full_name, email, current_address, permanent_address

    def check_filled_form(self):
        full_name = self.is_visible('css', self.locators.CREATED_FULL_NAME).text.split(":")[1]
        email = self.is_visible('css', self.locators.CREATED_EMAIL).text.split(":")[1]
        current_address = self.is_visible('css', self.locators.CREATED_CURRENT_ADDRESS).text.split(":")[1]
        permanent_address = self.is_visible('css', self.locators.CREATED_PERMANENT_ADDRESS).text.split(":")[1]
        return full_name, email, current_address, permanent_address


class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()

    def open_full_list(self):
        self.is_visible('css', self.locators.EXPAND_ALL_BUTTON).click()

    def click_random_checkbox(self):
        item_list = self.are_visible('css', self.locators.ITEM_LIST)
        count = 21
        while count != 0:
            item = item_list[random.randint(1, 15)]
            if count > 0:
                self.go_to_element(item)
                item.click()
                count -= 1
            else:
                break

    def get_checked_checkboxes(self):
        checked_list = self.are_present('css', self.locators.CHECKED_ITEMS)
        data = []
        for box in checked_list:
            title_item = box.find_element_by_xpath(self.locators.TITLE_ITEM)
            data.append(title_item.text)
        return str(data).replace(' ', '').replace('doc', '').replace('.', '').lower()

    def get_output_result(self):
        result_list = self.are_present('css', self.locators.OUTPUT_RESULT)
        data = []
        for item in result_list:
            data.append(item.text)
        return str(data).replace(' ', '').lower()


class RadioButtonPage(BasePage):
    locators = RadioButtonPageLocators()

    def click_on_radio_button(self, choice):
        choices = {'yes': self.locators.YES_RADIOBUTTON,
                  'impressive': self.locators.IMPRESSIVE_RADIOBUTTON,
                  'no': self.locators.NO_RADIOBUTTON}
        self.is_visible('css', choices[choice]).click()

    def get_output_result(self):
        return self.is_present('css', self.locators.OUTPUT_RESULT).text
