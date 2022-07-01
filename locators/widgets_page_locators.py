class AccordianPageLocators:
    SECTION_FIRST = "div[id='section1Heading']"
    SECTION_CONTENT_FIRST = "div[id='section1Content'] p"
    SECTION_SECOND = "div[id='section2Heading']"
    SECTION_CONTENT_SECOND = "div[id='section2Content'] p"
    SECTION_THIRD = "div[id='section3Heading']"
    SECTION_CONTENT_THIRD = "div[id='section3Content'] p"


class AutoCompletePageLocators:
    MULTI_INPUT = "input[id='autoCompleteMultipleInput']"
    MULTI_VALUE = "div[class='css-1rhbuit-multiValue auto-complete__multi-value']"
    MULTI_VALUE_REMOVE = "div[class='css-1rhbuit-multiValue auto-complete__multi-value'] svg path"

    SINGLE_INPUT = "input[id='autoCompleteSingleInput']"
    SINGLE_CONTAINER = "div[id='autoCompleteSingleContainer']"


class DatePickerPageLocators:
    DATE_INPUT = "input[id='datePickerMonthYearInput']"
    DATE_SELECT_MONTH = "select[class='react-datepicker__month-select']"
    DATE_SELECT_YEAR = "select[class='react-datepicker__year-select']"
    DATE_SELECT_DAY_LIST = "div[class^='react-datepicker__day react-datepicker__day']"

    TIME_AND_DATE_INPUT = "input[id='dateAndTimePickerInput']"
    TIME_AND_DATE_MONTH = "div[class='react-datepicker__month-read-view']"
    TIME_AND_DATE_YEAR = "div[class='react-datepicker__year-read-view']"
    TIME_AND_DATE_TIME_LIST = "li[class='react-datepicker__time-list-item ']"
    TIME_AND_DATE_MONTH_LIST = "div[class='react-datepicker__month-option']"
    TIME_AND_DATE_YEAR_LIST = "div[class='react-datepicker__year-option']"
