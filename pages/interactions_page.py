import random
import re
import time

import allure

from locators.interactions_page_locators import SortablePageLocators, SelectablePageLocators, ResizablePageLocators, \
    DroppablePageLocators, DraggablePageLocators
from pages.base_page import BasePage


class SortablePage(BasePage):
    locators = SortablePageLocators()

    @allure.step('get sortable items')
    def get_sortable_items(self, elements):
        item_list = self.are_visible('css', elements)
        return [item.text for item in item_list]

    @allure.step('change order')
    def change_order(self, order_name):
        order = {'list':
                     {'name': self.locators.TAB_LIST,
                      'item': self.locators.LIST_ITEM},
                 'grid':
                     {'name': self.locators.TAB_GRID,
                      'item': self.locators.GRID_ITEM},
                 }
        self.is_visible('css', order[order_name]['name']).click()
        order_before = self.get_sortable_items(order[order_name]['item'])
        item_list = random.sample(self.are_visible('css', order[order_name]['item']), k=2)
        item_what = item_list[0]
        item_where = item_list[1]
        self.action_drag_and_drop_to_element(item_what, item_where)
        order_after = self.get_sortable_items(order[order_name]['item'])
        return order_before, order_after


class SelectablePage(BasePage):
    locators = SelectablePageLocators()

    @allure.step('click selectable item')
    def click_selectable_item(self, elements):
        item_list = self.are_visible('css', elements)
        random.sample(item_list, k=1)[0].click()

    @allure.step('select item')
    def select_item(self, order_name):
        order = {'list':
                     {'name': self.locators.TAB_LIST,
                      'item': self.locators.LIST_ITEM,
                      'item_active': self.locators.LIST_ITEM_ACTIVE},
                 'grid':
                     {'name': self.locators.TAB_GRID,
                      'item': self.locators.GRID_ITEM,
                      'item_active': self.locators.GRID_ITEM_ACTIVE},
                 }
        self.is_visible('css', order[order_name]['name']).click()
        self.click_selectable_item(order[order_name]['item'])
        active_element = self.is_visible('css', order[order_name]['item_active'])
        return active_element.text


class ResizablePage(BasePage):
    locators = ResizablePageLocators()

    @allure.step('get px from width and height')
    def get_px_from_width_height(self, value_of_size):
        width = value_of_size.split(';')[0].split(':')[1].replace(' ', '')
        height = value_of_size.split(';')[1].split(':')[1].replace(' ', '')
        return width, height

    @allure.step('get max and min size')
    def get_max_min_size(self, element):
        size = self.is_present('css', element)
        size_value = size.get_attribute('style')
        return size_value

    @allure.step('change size resizable box')
    def change_size_resizable_box(self):
        self.action_drag_and_drop_by_offset(self.is_present('css', self.locators.RESIZABLE_BOX_HANDLE), 400, 200)
        max_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE_BOX))
        self.action_drag_and_drop_by_offset(self.is_present('css', self.locators.RESIZABLE_BOX_HANDLE), -400, -200)
        min_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE_BOX))
        return max_size, min_size

    @allure.step('change size resizable')
    def change_size_resizable(self):
        self.action_drag_and_drop_by_offset(self.is_visible('css', self.locators.RESIZABLE_HANDLE),
                                            random.randint(1, 300), random.randint(1, 300))
        max_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE))
        self.action_drag_and_drop_by_offset(self.is_visible('css', self.locators.RESIZABLE_HANDLE),
                                            random.randint(-200, -1), random.randint(-200, -1))
        min_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE))
        return max_size, min_size


class DroppablePage(BasePage):
    locators = DroppablePageLocators()

    @allure.step('drop simple div')
    def drop_simple(self):
        self.is_visible('css', self.locators.SIMPLE_TAB).click()
        drag_div = self.is_visible('css', self.locators.DRAG_ME_SIMPLE)
        drop_div = self.is_visible('css', self.locators.DROP_HERE_SIMPLE)
        self.action_drag_and_drop_to_element(drag_div, drop_div)
        return drop_div.text

    @allure.step('drop accept div')
    def drop_accept(self):
        self.is_visible('css', self.locators.ACCEPT_TAB).click()
        acceptable_div = self.is_visible('css', self.locators.ACCEPTABLE)
        not_acceptable_div = self.is_visible('css', self.locators.NOT_ACCEPTABLE)
        drop_div = self.is_visible('css', self.locators.DROP_HERE_ACCEPT)
        self.action_drag_and_drop_to_element(not_acceptable_div, drop_div)
        drop_text_not_accept = drop_div.text
        self.action_drag_and_drop_to_element(acceptable_div, drop_div)
        drop_text_accept = drop_div.text
        return drop_text_not_accept, drop_text_accept

    @allure.step('drop prevent propogation div')
    def drop_prevent_propogation(self):
        self.is_visible('css', self.locators.PREVENT_TAB).click()
        drag_div = self.is_visible('css', self.locators.DRAG_ME_PREVENT)
        not_greedy_inner_box = self.is_visible('css', self.locators.NOT_GREEDY_INNER_BOX)
        greedy_inner_box = self.is_visible('css', self.locators.GREEDY_INNER_BOX)
        self.action_drag_and_drop_to_element(drag_div, not_greedy_inner_box)
        text_not_greedy_box = self.is_visible('css', self.locators.NOT_GREEDY_DROP_BOX_TEXT).text
        text_not_greedy_inner_box = not_greedy_inner_box.text
        self.action_drag_and_drop_to_element(drag_div, greedy_inner_box)
        text_greedy_box = self.is_visible('css', self.locators.GREEDY_DROP_BOX_TEXT).text
        text_greedy_inner_box = greedy_inner_box.text
        return text_not_greedy_box, text_not_greedy_inner_box, text_greedy_box, text_greedy_inner_box

    @allure.step('drag revert draggable div')
    def drop_revert_draggable(self, type_drag):
        drag = {'will':
                    {'revert': self.locators.WILL_REVERT},
                'not_will':
                    {'revert': self.locators.NOT_REVERT},
                }
        self.is_visible('css', self.locators.REVERT_TAB).click()
        revert = self.is_visible('css', drag[type_drag]['revert'])
        drop_div = self.is_visible('css', self.locators.DROP_HERE_REVERT)
        self.action_drag_and_drop_to_element(revert, drop_div)
        position_after_move = revert.get_attribute('style')
        time.sleep(1)
        position_after_revert = revert.get_attribute('style')
        return position_after_move, position_after_revert


class DraggablePage(BasePage):
    locators = DraggablePageLocators()

    @allure.step('get before and after positions')
    def get_before_and_after_position(self, drag_element):
        self.action_drag_and_drop_by_offset(drag_element, random.randint(0, 50), random.randint(0, 50))
        before_position = drag_element.get_attribute('style')
        self.action_drag_and_drop_by_offset(drag_element, random.randint(0, 50), random.randint(0, 50))
        after_position = drag_element.get_attribute('style')
        return before_position, after_position

    @allure.step('simple drag and drop')
    def simple_drag_box(self):
        self.is_visible('css', self.locators.SIMPLE_TAB).click()
        drag_div = self.is_visible('css', self.locators.DRAG_ME)
        before_position, after_position = self.get_before_and_after_position(drag_div)
        return before_position, after_position

    @allure.step('get top position')
    def get_top_position(self, position):
        return re.findall(r'\d[0-9]|\d', position.split(';')[2])

    @allure.step('get left position')
    def get_left_position(self, position):
        return re.findall(r'\d[0-9]|\d', position.split(';')[1])

    @allure.step('drag box')
    def axis_restricted_drag_box(self, type_drag):
        drag = {'x':
                    {'only': self.locators.ONLY_X},
                'y':
                    {'only': self.locators.ONLY_Y},
                }
        self.is_visible('css', self.locators.AXIS_TAB).click()
        only = self.is_visible('css', drag[type_drag]['only'])
        position = self.get_before_and_after_position(only)
        top_before = self.get_top_position(position[0])
        top_after = self.get_top_position(position[1])
        left_before = self.get_left_position(position[0])
        left_after = self.get_left_position(position[1])
        return top_before, top_after, left_before, left_after
