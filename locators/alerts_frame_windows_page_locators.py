class BrowserWindowsPageLocators:
    BUTTON_NEW_TAB = "button[id='tabButton']"
    BUTTON_NEW_WINDOW = "button[id='windowButton']"

    TITLE_NEW_TAB = "h1[id='sampleHeading']"


class AlertsPageLocators:
    BUTTON_SEE_ALERT = "button[id='alertButton']"
    BUTTON_APPEAR_ALERT_AFTER_5_SEC = "button[id='timerAlertButton']"
    BUTTON_CONFIRM_ALERT = "button[id='confirmButton']"
    BUTTON_PROMPT_ALERT = "button[id='promtButton']"
    CONFIRM_RESULT = "span[id='confirmResult'"
    PROMPT_RESULT = "span[id='promptResult'"


class FramePageLocators:
    FIRST_FRAME = "iframe[id='frame1']"
    SECOND_FRAME = "iframe[id='frame2']"
    TITLE_FRAME = "h1[id='sampleHeading']"


class NestedFramesPageLocators:
    PARENT_FRAME = "iframe[id='frame1']"
    PARENT_TEXT = "body"
    CHILD_FRAME = "iframe[srcdoc='<p>Child Iframe</p>']"
    CHILD_TEXT = "p"
