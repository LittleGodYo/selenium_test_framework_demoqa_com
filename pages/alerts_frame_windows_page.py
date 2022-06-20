from locators.alerts_frame_windows_page_locators import BrowserWindowsPageLocators
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