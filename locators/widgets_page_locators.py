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
