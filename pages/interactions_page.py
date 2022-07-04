import random
import time

from locators.interactions_page_locators import SortablePageLocators, SelectablePageLocators, ResizablePageLocators, \
    DroppablePageLocators
from pages.base_page import BasePage


class SortablePage(BasePage):
    locators = SortablePageLocators()

    def get_sortable_items(self, elements):
        item_list = self.are_visible('css', elements)
        return [item.text for item in item_list]

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

    def click_selectable_item(self, elements):
        item_list = self.are_visible('css', elements)
        random.sample(item_list, k=1)[0].click()

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

    def get_px_from_width_height(self, value_of_size):
        width = value_of_size.split(';')[0].split(':')[1].replace(' ', '')
        height = value_of_size.split(';')[1].split(':')[1].replace(' ', '')
        return width, height

    def get_max_min_size(self, element):
        size = self.is_present('css', element)
        size_value = size.get_attribute('style')
        return size_value

    def change_size_resizable_box(self):
        self.action_drag_and_drop_by_offset(self.is_present('css', self.locators.RESIZABLE_BOX_HANDLE), 400, 200)
        max_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE_BOX))
        self.action_drag_and_drop_by_offset(self.is_present('css', self.locators.RESIZABLE_BOX_HANDLE), -400, -200)
        min_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE_BOX))
        return max_size, min_size

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

    def drop_simple(self):
        self.is_visible('css', self.locators.SIMPLE_TAB).click()
        drag_div = self.is_visible('css', self.locators.DRAG_ME_SIMPLE)
        drop_div = self.is_visible('css', self.locators.DROP_HERE_SIMPLE)
        self.action_drag_and_drop_to_element(drag_div, drop_div)
        return drop_div.text

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
