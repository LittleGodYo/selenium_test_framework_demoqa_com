import base64
import os
import random

import requests
from selenium.webdriver.common.by import By

from generator.generator import generated_person, generated_file
from pages.base_page import BasePage
from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonPageLocators, \
    WebTablePageLocators, ButtonsPageLocators, LinksPageLocators, UploadAndDownloadPageLocators


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


class WebTablePage(BasePage):
    locators = WebTablePageLocators()

    def add_new_person(self):
        count = random.randint(1, 5)
        while count != 0:
            person_info = next(generated_person())
            first_name = person_info.first_name
            last_name = person_info.last_name
            email = person_info.email
            age = person_info.age
            salary = person_info.salary
            department = person_info.department
            self.is_visible('css', self.locators.BUTTON_ADD).click()
            self.is_visible('css', self.locators.INPUT_FIRST_NAME).send_keys(first_name)
            self.is_visible('css', self.locators.INPUT_LAST_NAME).send_keys(last_name)
            self.is_visible('css', self.locators.INPUT_EMAIL).send_keys(email)
            self.is_visible('css', self.locators.INPUT_AGE).send_keys(age)
            self.is_visible('css', self.locators.INPUT_SALARY).send_keys(salary)
            self.is_visible('css', self.locators.INPUT_DEPARTMENT).send_keys(department)
            self.is_visible('css', self.locators.BUTTON_SUBMIT).click()
            count -= 1
        return [first_name, last_name, str(age), email, str(salary), department]

    def check_added_person(self):
        people_list = self.are_present('css', self.locators.FULL_PEOPLE_LIST)
        data = []
        for item in people_list:
            data.append(item.text.splitlines())
        return data

    def search_some_person(self, key_word):
        self.is_visible("css", self.locators.INPUT_SEARCH).send_keys(key_word)

    def check_search_person(self):
        delete_button = self.is_visible('css', self.locators.BUTTON_DELETE)
        row = delete_button.find_element_by_xpath(self.locators.ROW_PARENT)
        return row.text.splitlines()

    def update_person_info(self):
        person_info = next(generated_person())
        age = person_info.age
        self.is_visible('css', self.locators.BUTTON_UPDATE).click()
        self.is_visible('css', self.locators.INPUT_AGE).clear()
        self.is_visible('css', self.locators.INPUT_AGE).send_keys(age)
        self.is_visible('css', self.locators.BUTTON_SUBMIT).click()
        return str(age)

    def delete_person_info(self):
        self.is_visible('css', self.locators.BUTTON_DELETE).click()

    def check_deleted(self):
        return self.is_present('css', self.locators.NO_ROWS_FOUND).text

    def select_up_to_some_rows(self):
        count = [5, 10, 20, 25, 50, 100]
        data = []
        for x in count:
            count_row_button = self.is_present('css', self.locators.COUNT_ROWS_LIST)
            self.go_to_element(count_row_button)
            count_row_button.click()
            self.is_visible((By.CSS_SELECTOR, f'option[value="{x}"')).click()
            data.append(self.check_count_rows())
        return data

    def check_count_rows(self):
        list_rows = self.are_present('css', self.locators.FULL_PEOPLE_LIST)
        return len(list_rows)


class ButtonsPage(BasePage):
    locators = ButtonsPageLocators()

    def click_on_different_button(self, type_click):
        if type_click == "double":
            self.action_double_click(self.is_visible('css', self.locators.BUTTON_DOUBLE_CLICK))
            return self.check_clicked_on_the_button(self.locators.SUCCESS_DOUBLE)
        if type_click == "right":
            self.action_right_click(self.is_visible('css', self.locators.BUTTON_RIGHT_CLICK))
            return self.check_clicked_on_the_button(self.locators.SUCCESS_RIGHT)
        if type_click == "click":
            self.is_visible('xpath', self.locators.BUTTON_CLICK_ME).click()
            return self.check_clicked_on_the_button(self.locators.SUCCESS_CLICK_ME)

    def check_clicked_on_the_button(self, element):
        return self.is_present('css', element).text


class LinksPage(BasePage):
    locators = LinksPageLocators()

    def check_new_tab_simple_link(self):
        simple_link = self.is_visible('css', self.locators.SIMPLE_LINK)
        link_href = simple_link.get_attribute('href')
        request = requests.get(link_href)
        if request.status_code == 200:
            simple_link.click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            url = self.driver.current_url
            return link_href, url
        else:
            return link_href, request.status_code

    def check_broken_link(self, url):
        request = requests.get(url)
        if request.status_code == 200:
            self.is_present('css', self.locators.BAD_REQUEST).click()
        else:
            return request.status_code


class UploadAndDownloadPage(BasePage):
    locators = UploadAndDownloadPageLocators()

    def upload_file(self):
        file_name, path = generated_file()
        self.is_present('css', self.locators.UPLOAD_FILE).send_keys(path)
        os.remove(path)
        text = self.is_visible('css', self.locators.UPLOADED_FILE).text
        return file_name.split('\\')[-1], text.split('\\')[-1]

    def download_file(self):
        link = self.is_present('css', self.locators.DOWNLOAD_FILE).get_attribute('href')
        link_b = base64.b64decode(link)
        path_name_file = rf'D:\down\{random.randint(0, 999)}.jpg'
        with open(path_name_file, 'wb+') as f:
            offset = link_b.find(b'\xff\xd8')
            f.write(link_b[offset:])
            check_file = os.path.exists(path_name_file)
            f.close()
        os.remove(path_name_file)
        return check_file

