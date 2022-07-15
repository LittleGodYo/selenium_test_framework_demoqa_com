import random
import time

import allure
from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select

from generator.generator import generated_color, generated_date
from locators.widgets_page_locators import AccordianPageLocators, AutoCompletePageLocators, DatePickerPageLocators, \
    ProgressBarPageLocators, SliderPageLocators, TabsPageLocators, ToolsTipsPageLocators, MenuPageLocators
from pages.base_page import BasePage


class AccordianPage(BasePage):
    locators = AccordianPageLocators()

    @allure.step('check accordian widget')
    def check_accordian(self, accordian_num):
        accordian = {'first':
                         {'title': self.locators.SECTION_FIRST,
                          'content': self.locators.SECTION_CONTENT_FIRST},
                     'second':
                         {'title': self.locators.SECTION_SECOND,
                          'content': self.locators.SECTION_CONTENT_SECOND},
                     'third':
                         {'title': self.locators.SECTION_THIRD,
                          'content': self.locators.SECTION_CONTENT_THIRD},
                     }
        section_title = self.is_visible('css', accordian[accordian_num]["title"])
        section_title.click()
        try:
            section_content = self.is_visible('css', accordian[accordian_num]["content"]).text
        except TimeoutException:
            section_title.click()
            section_content = self.is_visible('css', accordian[accordian_num]["content"]).text
        return [section_title.text, len(section_content)]


class AutoCompletePage(BasePage):
    locators = AutoCompletePageLocators()

    @allure.step('fill multi autocomplete input')
    def fill_input_multi(self):
        colors = random.sample(next(generated_color()).color_name, k=random.randint(2, 5))
        for color in colors:
            input_multi = self.is_clickable('css', self.locators.MULTI_INPUT)
            input_multi.send_keys(color)
            input_multi.send_keys(Keys.ENTER)
        return colors

    @allure.step('remove value from multi autocomplete')
    def remove_value_from_multi(self):
        count_value_before = len(self.are_present('css', self.locators.MULTI_VALUE))
        remove_button_list = self.are_visible('css', self.locators.MULTI_VALUE_REMOVE)
        for value in remove_button_list:
            value.click()
            break
        count_value_after = len(self.are_present('css', self.locators.MULTI_VALUE))
        return count_value_before, count_value_after

    @allure.step('check colors in multi autocomplete')
    def check_color_in_multi(self):
        color_list = self.are_present('css', self.locators.MULTI_VALUE)
        colors = []
        for color in color_list:
            colors.append(color.text)
        return colors

    @allure.step('fill single autocomplete input')
    def fill_input_single(self):
        color = random.sample(next(generated_color()).color_name, k=1)
        input_single = self.is_clickable('css', self.locators.SINGLE_INPUT)
        input_single.send_keys(color)
        input_single.send_keys(Keys.ENTER)
        return color[0]

    @allure.step('check color in single autocomplete')
    def check_color_in_single(self):
        color = self.is_visible('css', self.locators.SINGLE_CONTAINER)
        return color.text.split()[3]


class DatePickerPage(BasePage):
    locators = DatePickerPageLocators()

    @allure.step('change date')
    def select_date(self):
        date = next(generated_date())
        input_date = self.is_visible('css', self.locators.DATE_INPUT)
        value_date_before = input_date.get_attribute('value')
        input_date.click()
        self.set_date_by_text(self.locators.DATE_SELECT_MONTH, date.month)
        self.set_date_by_text(self.locators.DATE_SELECT_YEAR, date.year)
        self.set_date_item_from_list(self.locators.DATE_SELECT_DAY_LIST, date.day)
        value_date_after = input_date.get_attribute('value')
        return value_date_before, value_date_after

    @allure.step('change select date and time')
    def select_date_and_time(self):
        date = next(generated_date())
        input_date = self.is_visible('css', self.locators.TIME_AND_DATE_INPUT)
        value_date_before = input_date.get_attribute('value')
        input_date.click()
        self.is_visible('css', self.locators.TIME_AND_DATE_MONTH).click()
        self.set_date_item_from_list(self.locators.TIME_AND_DATE_MONTH_LIST, date.month)
        self.is_visible('css', self.locators.TIME_AND_DATE_YEAR).click()
        self.set_date_item_from_list(self.locators.TIME_AND_DATE_YEAR_LIST, '2020')
        self.set_date_item_from_list(self.locators.DATE_SELECT_DAY_LIST, date.day)
        self.set_date_item_from_list(self.locators.TIME_AND_DATE_TIME_LIST, date.time)
        input_date_after = self.is_visible('css', self.locators.TIME_AND_DATE_INPUT)
        value_date_after = input_date_after.get_attribute('value')
        return value_date_before, value_date_after

    @allure.step('select date by text')
    def set_date_by_text(self, element, value):
        select = Select(self.is_present('css', element))
        select.select_by_visible_text(value)

    @allure.step('select date item from list')
    def set_date_item_from_list(self, elements, value):
        item_list = self.are_present('css', elements)
        for item in item_list:
            if item.text == value:
                item.click()
                break


class SliderPage(BasePage):
    locators = SliderPageLocators()

    @allure.step('change slider value')
    def change_slider_value(self):
        value_before = self.is_visible('css', self.locators.SLIDER_VALUE).get_attribute('value')
        slider_input = self.is_visible('css', self.locators.INPUT_SLIDER)
        self.action_drag_and_drop_by_offset(slider_input, random.randint(1, 100), 0)
        value_after = self.is_visible('css', self.locators.SLIDER_VALUE).get_attribute('value')
        return value_before, value_after


class ProgressBarPage(BasePage):
    locators = ProgressBarPageLocators()

    @allure.step('change progress bar value')
    def change_progress_bar_value(self):
        progress_bar_button = self.is_visible('css', self.locators.BUTTON_PROGRESS_BAR)
        progress_bar_button.click()
        time.sleep(random.randint(1, 5))
        progress_bar_button.click()
        value = self.is_present('css', self.locators.PROGRESS_BAR_VALUE).text
        return int(value.replace('%', ''))


class TabsPage(BasePage):
    locators = TabsPageLocators()

    @allure.step('check tabs')
    def check_tabs(self, tab_name):
        tab = {'what':
                   {'title': self.locators.TABS_WHAT,
                    'content': self.locators.TABS_WHAT_CONTENT},
               'origin':
                   {'title': self.locators.TABS_ORIGIN,
                    'content': self.locators.TABS_ORIGIN_CONTENT},
               'use':
                   {'title': self.locators.TABS_USE,
                    'content': self.locators.TABS_USE_CONTENT},
               'more':
                   {'title': self.locators.TABS_MORE,
                    'content': self.locators.TABS_MORE_CONTENT},
               }
        tab_title = self.is_visible('css', tab[tab_name]["title"])
        tab_title.click()
        tab_content = self.is_visible('css', tab[tab_name]["content"]).text
        return tab_content


class ToolsTipsPage(BasePage):
    locators = ToolsTipsPageLocators()

    @allure.step('get text from tool tips')
    def get_text_from_tool_tips(self, hover_name):
        hover = {'button':
                     {'hover': self.locators.BUTTON_HOVER_ME_TO_SEE,
                      'wait': self.locators.TOOL_TIP_BUTTON,
                      'by': 'css'},
                 'field':
                     {'hover': self.locators.FIELD_HOVER_ME_TO_SEE,
                      'wait': self.locators.TOOL_TIP_FIELD,
                      'by': 'css'},
                 'contrary':
                     {'hover': self.locators.CONTRARY_LINK,
                      'wait': self.locators.TOOL_TIP_CONTRARY,
                      'by': 'xpath'},
                 'section':
                     {'hover': self.locators.SECTION_LINK,
                      'wait': self.locators.TOOL_TIP_SECTION,
                      'by': 'xpath'},
                 }
        element = self.is_present(hover[hover_name]["by"], hover[hover_name]["hover"])
        self.action_move_to_element(element)
        self.is_visible('css', hover[hover_name]["wait"])
        self.action_move_to_element(element)
        tool_tip_text = self.is_present('css', self.locators.TOOL_TIPS_INNERS)
        text = tool_tip_text.text
        return text


class MenuPage(BasePage):
    locators = MenuPageLocators()

    @allure.step('check menu item')
    def check_menu(self):
        menu_item_list = self.are_present('css', self.locators.MENU_ITEMS_LIST)
        data = []
        for item in menu_item_list:
            self.action_move_to_element(item)
            data.append(item.text)
        return data
