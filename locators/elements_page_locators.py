class TextBoxPageLocators:
    FULL_NAME = "input[id='userName']"
    EMAIL = "input[id='userEmail']"
    CURRENT_ADDRESS = "textarea[id='currentAddress']"
    PERMANENT_ADDRESS = "textarea[id='permanentAddress']"
    SUBMIT = "button[id='submit']"

    CREATED_FULL_NAME = "#output #name"
    CREATED_EMAIL = "#output #email"
    CREATED_CURRENT_ADDRESS = "#output #currentAddress"
    CREATED_PERMANENT_ADDRESS = "#output #permanentAddress"


class CheckBoxPageLocators:
    EXPAND_ALL_BUTTON = "button[title='Expand all']"
    ITEM_LIST = "span[class='rct-title']"
    CHECKED_ITEMS = "svg[class='rct-icon rct-icon-check']"
    TITLE_ITEM = ".//ancestor::span[@class='rct-text']"
    OUTPUT_RESULT = "span[class='text-success']"
