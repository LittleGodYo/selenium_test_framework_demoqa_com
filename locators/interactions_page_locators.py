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


class DroppablePageLocators:
    # Simple
    SIMPLE_TAB = "a[id='droppableExample-tab-simple']"
    DRAG_ME_SIMPLE = "div[id='draggable']"
    DROP_HERE_SIMPLE = "#simpleDropContainer #droppable"

    # Accept
    ACCEPT_TAB = "a[id='droppableExample-tab-accept']"
    ACCEPTABLE = "div[id='acceptable']"
    NOT_ACCEPTABLE = "div[id='notAcceptable']"
    DROP_HERE_ACCEPT = "#acceptDropContainer #droppable"

    # Prevent Propogation
    PREVENT_TAB = "a[id='droppableExample-tab-preventPropogation']"
    NOT_GREEDY_DROP_BOX_TEXT = "div[id='notGreedyDropBox'] p:nth-child(1)"
    NOT_GREEDY_INNER_BOX = "div[id='notGreedyInnerDropBox']"
    GREEDY_DROP_BOX_TEXT = "div[id='greedyDropBox'] p:nth-child(1)"
    GREEDY_INNER_BOX = "div[id='greedyDropBoxInner']"
    DRAG_ME_PREVENT = "#ppDropContainer #dragBox"

    # Revert Draggable
    REVERT_TAB = "a[id='droppableExample-tab-revertable']"
    WILL_REVERT = "div[id='revertable']"
    NOT_REVERT = "div[id='notRevertable']"
    DROP_HERE_REVERT = "#revertableDropContainer #droppable"


class DraggablePageLocators:
    #Simple
    SIMPLE_TAB = "a[id='draggableExample-tab-simple']"
    DRAG_ME = "div[id='draggableExample-tabpane-simple'] div[id='dragBox']"

    #Axis Restricted
    AXIS_TAB = "a[id='draggableExample-tab-axisRestriction']"
    ONLY_X = "div[id='restrictedX']"
    ONLY_Y = "div[id='restrictedY']"
