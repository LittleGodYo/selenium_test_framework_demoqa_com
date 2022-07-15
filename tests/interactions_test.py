import allure

from pages.interactions_page import SortablePage, SelectablePage, ResizablePage, DroppablePage, DraggablePage


@allure.suite('Interactions')
class TestInteractions:

    @allure.feature('Sortable Page')
    class TestSortablePage:

        @allure.title('Check changed sortable list and grid')
        def test_sortable(self, driver):
            sortable = SortablePage(driver, 'https://demoqa.com/sortable')
            sortable.open()
            list_before, list_after = sortable.change_order('list')
            grid_before, grid_after = sortable.change_order('grid')
            assert list_before != list_after, 'The order of the list has not been changed'
            assert grid_before != grid_after, 'The order of the grid has not been changed'

    @allure.feature('Selectable Page')
    class TestSelectablePage:

        @allure.title('Check changed selectable list and grid')
        def test_selectable(self, driver):
            selectable = SelectablePage(driver, 'https://demoqa.com/selectable')
            selectable.open()
            active_list = selectable.select_item('list')
            active_grid = selectable.select_item('grid')
            assert len(active_list) > 0, 'No elements were selected'
            assert len(active_grid) > 0, 'No elements were selected'

    @allure.feature('Resizable Page')
    class TestResizablePage:

        @allure.title('Check changed resizable boxes')
        def test_resizable(self, driver):
            resizable = ResizablePage(driver, 'https://demoqa.com/resizable')
            resizable.open()
            max_box, min_box = resizable.change_size_resizable_box()
            max_resize, min_resize = resizable.change_size_resizable()
            assert ('500px', '300px') == max_box, 'Maximum size not equal to "500px", "300px"'
            assert ('150px', '150px') == min_box, 'Minimum size not equal to "150px", "150px"'
            assert min_resize != max_resize, "Resizable has not been changed"

    @allure.feature('Droppable Page')
    class TestDroppablePage:

        @allure.title('Check simple droppable')
        def test_simple_droppable(self, driver):
            droppable = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable.open()
            text = droppable.drop_simple()
            assert text == 'Dropped!', 'The elements have not been dropped'

        @allure.title('Check accept droppable')
        def test_accept_droppable(self, driver):
            droppable = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable.open()
            drop_text_not_accept, drop_text_accept = droppable.drop_accept()
            assert drop_text_not_accept == 'Drop here', 'The dropped has been accepted'
            assert drop_text_accept == 'Dropped!', 'The dropped has not been accepted'

        @allure.title('Check prevent propagation droppable')
        def test_prevent_droppable(self, driver):
            droppable = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable.open()
            not_greedy, not_greedy_inner, greedy, greedy_inner = droppable.drop_prevent_propogation()
            assert not_greedy == 'Dropped!', 'The elements have not been changed'
            assert not_greedy_inner == 'Dropped!', 'The elements have not been changed'
            assert greedy == 'Outer droppable', 'The elements have been changed'
            assert greedy_inner == 'Dropped!', 'The elements have not been changed'

        @allure.title('Check revert draggable droppable')
        def test_revert_draggable_droppable(self, driver):
            droppable = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable.open()
            will_after_move, will_after_revert = droppable.drop_revert_draggable('will')
            not_will_after_move, not_will_after_revert = droppable.drop_revert_draggable('not_will')
            assert will_after_move != will_after_revert, 'The elements have not reverted'
            assert not_will_after_move == not_will_after_revert, 'The elements have reverted'

    @allure.feature('Draggable Page')
    class TestDraggablePage:

        @allure.title('Check simple draggable')
        def test_simple_draggable(self, driver):
            draggable = DraggablePage(driver, 'https://demoqa.com/dragabble')
            draggable.open()
            before_position, after_position = draggable.simple_drag_box()
            assert before_position != after_position, "The position of the box has not been changed"

        @allure.title('Check axis restricted draggable')
        def test_axis_restricted_draggable(self, driver):
            draggable = DraggablePage(driver, 'https://demoqa.com/dragabble')
            draggable.open()
            top_x_before, top_x_after, left_x_before, left_x_after = draggable.axis_restricted_drag_box('x')
            top_y_before, top_y_after, left_y_before, left_y_after = draggable.axis_restricted_drag_box('y')
            assert top_x_before == top_x_after and int(top_x_after[0]) == 0, "Box position has not been changed or " \
                                                                             "there has been a shift in the y-axis "
            assert left_x_before != left_x_after and int(left_x_after[0]) != 0, "Box position has not been changed or " \
                                                                                "there has been a shift in the y-axis "
            assert top_y_before != top_y_after and int(top_y_after[0]) != 0, "Box position has not been changed or " \
                                                                             "there has been a shift in the x-axis "
            assert left_y_before == left_y_after and int(left_y_after[0]) == 0, "Box position has not been changed or " \
                                                                                "there has been a shift in the x-axis "



