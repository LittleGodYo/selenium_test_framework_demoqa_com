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


class SliderPageLocators:
    INPUT_SLIDER = "input[class='range-slider range-slider--primary']"
    SLIDER_VALUE = "input[id='sliderValue']"


class ProgressBarPageLocators:
    BUTTON_PROGRESS_BAR = "button[id='startStopButton']"
    PROGRESS_BAR_VALUE = "div[class='progress-bar bg-info']"


class TabsPageLocators:
    TABS_WHAT = "a[id='demo-tab-what']"
    TABS_WHAT_CONTENT = "div[id='demo-tabpane-what']"
    TABS_ORIGIN = "a[id='demo-tab-origin']"
    TABS_ORIGIN_CONTENT = "div[id='demo-tabpane-origin']"
    TABS_USE = "a[id='demo-tab-use']"
    TABS_USE_CONTENT = "div[id='demo-tabpane-use']"
    TABS_MORE = "a[id='demo-tab-more']"
    TABS_MORE_CONTENT = "div[id='demo-tabpane-more']"


class ToolsTipsPageLocators:
    BUTTON_HOVER_ME_TO_SEE = "button[id='toolTipButton']"
    TOOL_TIP_BUTTON = "button[aria-describedby='buttonToolTip']"

    FIELD_HOVER_ME_TO_SEE = "input[id='toolTipTextField']"
    TOOL_TIP_FIELD = "input[aria-describedby='textFieldToolTip']"

    CONTRARY_LINK = "//*[.='Contrary']"
    TOOL_TIP_CONTRARY = "a[aria-describedby='contraryTexToolTip']"

    SECTION_LINK = "//*[.='1.10.32']"
    TOOL_TIP_SECTION = "a[aria-describedby='sectionToolTip']"

    TOOL_TIPS_INNERS = "div[class='tooltip-inner']"
