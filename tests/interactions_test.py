from pages.interactions_page import SortablePage, SelectablePage, ResizablePage


class TestInteractions:
    class TestSortablePage:
        def test_sortable(self, driver):
            sortable = SortablePage(driver, 'https://demoqa.com/sortable')
            sortable.open()
            list_before, list_after = sortable.change_order('list')
            grid_before, grid_after = sortable.change_order('grid')
            assert list_before != list_after, 'The order of the list has not been changed'
            assert grid_before != grid_after, 'The order of the grid has not been changed'

    class TestSelectablePage:
        def test_selectable(self, driver):
            selectable = SelectablePage(driver, 'https://demoqa.com/selectable')
            selectable.open()
            active_list = selectable.select_item('list')
            active_grid = selectable.select_item('grid')
            assert len(active_list) > 0, 'No elements were selected'
            assert len(active_grid) > 0, 'No elements were selected'

    class TestResizablePage:
        def test_resizable(self, driver):
            resizable = ResizablePage(driver, 'https://demoqa.com/resizable')
            resizable.open()
            max_box, min_box = resizable.change_size_resizable_box()
            max_resize, min_resize = resizable.change_size_resizable()
            assert ('500px', '300px') == max_box, 'Maximum size not equal to "500px", "300px"'
            assert ('150px', '150px') == min_box, 'Minimum size not equal to "150px", "150px"'
            assert min_resize != max_resize, "Resizable has not been changed"

