import random

from locators.interactions_page_locators import SortablePageLocators, SelectablePageLocators
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


