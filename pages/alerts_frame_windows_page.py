import random
import time

from locators.alerts_frame_windows_page_locators import BrowserWindowsPageLocators, AlertsPageLocators
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