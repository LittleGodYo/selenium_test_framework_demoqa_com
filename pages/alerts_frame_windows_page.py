import random
import time

from locators.alerts_frame_windows_page_locators import BrowserWindowsPageLocators, AlertsPageLocators, \
    FramePageLocators, NestedFramesPageLocators
from pages.base_page import BasePage


class BrowserWindowsPage(BasePage):
    locators = BrowserWindowsPageLocators()

    def check_opened_new_tab_or_window(self, new):
        if new == 'new-tab':
            self.is_visible('css', self.locators.BUTTON_NEW_TAB).click()
        if new == 'new-window':
            self.is_visible('css', self.locators.BUTTON_NEW_WINDOW).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text_title = self.is_visible('css', self.locators.TITLE_NEW_TAB).text
        return text_title


class AlertsPage(BasePage):
    locators = AlertsPageLocators()

    def check_see_alert(self):
        self.is_visible('css', self.locators.BUTTON_SEE_ALERT).click()
        alert_window = self.use_alert()
        return alert_window.text

    def check_appear_5_sec(self):
        self.is_visible('css', self.locators.BUTTON_APPEAR_ALERT_AFTER_5_SEC).click()
        time.sleep(5)
        alert_window = self.use_alert()
        return alert_window.text

    def check_confirm_alert(self):
        self.is_visible('css', self.locators.BUTTON_CONFIRM_ALERT).click()
        alert_window = self.use_alert()
        alert_window.accept()
        text_result = self.is_present('css', self.locators.CONFIRM_RESULT).text
        return text_result

    def check_prompt_alert(self):
        text = f'autotest{random.randint(1, 100)}'
        self.is_visible('css', self.locators.BUTTON_PROMPT_ALERT).click()
        alert_window = self.use_alert()
        alert_window.send_keys(text)
        alert_window.accept()
        text_result = self.is_present('css', self.locators.PROMPT_RESULT).text
        return text, text_result


class FramePage(BasePage):
    locators = FramePageLocators()

    def check_frame(self, frame_num):
        if frame_num == 'frame1':
            frame = self.is_present('css', self.locators.FIRST_FRAME)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.use_frame(frame)
            text = self.is_present('css', self.locators.TITLE_FRAME).text
            self.driver.switch_to.default_content()
            return [text, width, height]
        if frame_num == 'frame2':
            frame = self.is_present('css', self.locators.SECOND_FRAME)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.use_frame(frame)
            text = self.is_present('css', self.locators.TITLE_FRAME).text
            return [text, width, height]


class NestedFramesPage(BasePage):
    locators = NestedFramesPageLocators()

    def check_nested_frame(self):
        parent_frame = self.is_present('css', self.locators.PARENT_FRAME)
        self.use_frame(parent_frame)
        parent_text = self.is_present('css', self.locators.PARENT_TEXT).text
        child_frame = self.is_present('css', self.locators.CHILD_FRAME)
        self.use_frame(child_frame)
        child_text = self.is_present('css', self.locators.CHILD_TEXT).text
        return parent_text, child_text
