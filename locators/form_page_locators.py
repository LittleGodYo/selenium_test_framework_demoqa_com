import random


class FormPageLocators:
    FIRST_NAME = "input[id='firstName']"
    LAST_NAME = "input[id='lastName']"
    EMAIL = "input[id='userEmail']"
    GENDER = f"div[class*='custom-control'] label[for='gender-radio-{random.randint(1, 3)}']"
    MOBILE = "input[id='userNumber']"
    SUBJECTS = "input[id='subjectsInput']"
    HOBBIES = f"div[class*='custom-control'] label[for='hobbies-checkbox-{random.randint(1, 3)}']"
    FILE_INPUT = "input[id='uploadPicture']"
    CURRENT_ADDRESS = "textarea[id='currentAddress']"
    STATE_SELECT = "div[id='state']"
    STATE_INPUT = "input[id='react-select-3-input']"
    CITY_SELECT = "div[id='city']"
    CITY_INPUT = "input[id='react-select-4-input']"
    SUBMIT = "button[id='submit']"

    RESULT_TABLE = "//div[@class='table-responsive']//td[2]"
