from pages.interactions_page import SortablePage


class TestInteractions:
    class TestSortablePage:
        def test_sortable(self, driver):
            sortable = SortablePage(driver, 'https://demoqa.com/sortable')
            sortable.open()
            list_before, list_after = sortable.change_order('list')
            grid_before, grid_after = sortable.change_order('grid')
            assert list_before != list_after, 'The order of the list has not been changed'
            assert grid_before != grid_after, 'The order of the grid has not been changed'
