import unittest
from src/app import GroceryList

class TestGroceryList(unittest.TestCase):
    def setUp(self):
        self.grocery_list = GroceryList()
        self.initial_items = ["Apples", "Bananas", "Milk", "Bread"]
        for item in self.initial_items:
            self.grocery_list.add_item(item)

    def test_add_item(self):
        new_item = "Eggs"
        self.grocery_list.add_item(new_item)
        self.assertIn(new_item, self.grocery_list.items)

    def test_remove_item(self):
        item_to_remove = "Milk"
        self.grocery_list.remove_item(item_to_remove)
        self.assertNotIn(item_to_remove, self.grocery_list.items)

    def test_mark_as_purchased(self):
        item_to_mark = "Bananas"
        self.grocery_list.mark_as_purchased(item_to_mark)
        self.assertNotIn(item_to_mark, self.grocery_list.items)

    def test_view_list(self):
        expected_output = "Grocery List:\n- Apples\n- Bananas\n- Milk\n- Bread"
        self.assertEqual(self.grocery_list.view_list(), expected_output)

if __name__ == "__main__":
    unittest.main()
