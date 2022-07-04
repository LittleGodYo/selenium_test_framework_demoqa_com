class SortablePageLocators:
    TAB_LIST = "a[id='demo-tab-list']"
    LIST_ITEM = "div[id='demo-tabpane-list'] div[class='list-group-item list-group-item-action']"
    TAB_GRID = "a[id='demo-tab-grid']"
    GRID_ITEM = "div[id='demo-tabpane-grid'] div[class='list-group-item list-group-item-action']"


class SelectablePageLocators:
    TAB_LIST = "a[id='demo-tab-list']"
    LIST_ITEM = "li[class='mt-2 list-group-item list-group-item-action']"
    LIST_ITEM_ACTIVE = "li[class='mt-2 list-group-item active list-group-item-action']"
    TAB_GRID = "a[id='demo-tab-grid']"
    GRID_ITEM = "li[class='list-group-item list-group-item-action']"
    GRID_ITEM_ACTIVE = "li[class='list-group-item active list-group-item-action']"


class ResizablePageLocators:
    RESIZABLE_BOX_HANDLE = "div[class='constraint-area'] span[class='react-resizable-handle react-resizable-handle-se']"
    RESIZABLE_BOX = "div[id='resizableBoxWithRestriction']"
    RESIZABLE_HANDLE = "div[id='resizable'] span[class='react-resizable-handle react-resizable-handle-se']"
    RESIZABLE = "div[id='resizable']"
