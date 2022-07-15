import os

import allure
from selenium.webdriver import Keys

from generator.generator import generated_person, generated_file
from locators.form_page_locators import FormPageLocators
from pages.base_page import BasePage


class FormPage(BasePage):
    locators = FormPageLocators()

    @allure.step('Fill in all fields')
    def fill_form_fields(self):
        person = next(generated_person())
        file_name, path = generated_file()
        self.is_visible('css', self.locators.FIRST_NAME).send_keys(person.first_name)
        self.is_visible('css', self.locators.LAST_NAME).send_keys(person.last_name)
        self.is_visible('css', self.locators.EMAIL).send_keys(person.email)
        self.is_visible('css', self.locators.GENDER).click()
        self.is_visible('css', self.locators.MOBILE).send_keys(person.mobile)
        self.is_visible('css', self.locators.SUBJECTS).send_keys('Hindi')
        self.is_visible('css', self.locators.SUBJECTS).send_keys(Keys.RETURN)
        self.is_visible('css', self.locators.HOBBIES).click()
        self.is_present('css', self.locators.FILE_INPUT).send_keys(path)
        os.remove(path)
        self.is_visible('css', self.locators.CURRENT_ADDRESS).send_keys(person.current_address)
        self.is_visible('css', self.locators.STATE_SELECT).click()
        self.is_visible('css', self.locators.STATE_INPUT).send_keys(Keys.RETURN)
        self.is_visible('css', self.locators.CITY_SELECT).click()
        self.is_visible('css', self.locators.CITY_INPUT).send_keys(Keys.RETURN)
        self.is_visible('css', self.locators.SUBMIT).send_keys(Keys.RETURN)
        return person

    @allure.step('Get form result')
    def form_result(self):
        result_list = self.are_present('xpath', self.locators.RESULT_TABLE)
        data = []
        for item in result_list:
            data.append(item.text)
        return data
