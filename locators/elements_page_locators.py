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


class RadioButtonPageLocators:
    YES_RADIOBUTTON = "div label[for='yesRadio']"
    IMPRESSIVE_RADIOBUTTON = "div label[for='impressiveRadio']"
    NO_RADIOBUTTON = "div label[for='noRadio']"
    OUTPUT_RESULT = "span[class=text-success]"


class WebTablePageLocators:
    BUTTON_ADD = "button[id='addNewRecordButton']"
    INPUT_FIRST_NAME = "input[id='firstName']"
    INPUT_LAST_NAME = "input[id='lastName']"
    INPUT_EMAIL = "input[id='userEmail']"
    INPUT_AGE = "input[id='age']"
    INPUT_SALARY = "input[id='salary']"
    INPUT_DEPARTMENT = "input[id='department']"
    BUTTON_SUBMIT = "button[id='submit']"

    FULL_PEOPLE_LIST = "div[class='rt-tr-group']"
    INPUT_SEARCH = "input[id='searchBox']"
    BUTTON_DELETE = "span[title='Delete']"
    ROW_PARENT = ".//ancestor::div[@class='rt-tr-group']"
    NO_ROWS_FOUND = "div[class='rt-noData']"
    COUNT_ROWS_LIST = "select[aria-label='rows per page']"

    BUTTON_UPDATE = "span[title='Edit']"


