import unittest
import os
from models.item import InventoryItem
from models.manager import InventoryManager

class TestManager(unittest.TestCase):

    def setUp(self):
        InventoryManager._instance = None
        self.manager = InventoryManager()
        self.manager._items.clear()
        self.test_file = "data/test_inventory.csv"

        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_add_item(self):
        item = InventoryItem("1", "Mouse", 10, 15, "Electronics")
        result = self.manager.add_item(item)

        self.assertTrue(result)
        self.assertEqual(len(self.manager._items), 1)

    def test_no_duplicate_id(self):
        item1 = InventoryItem("1", "Mouse", 10, 15, "Electronics")
        item2 = InventoryItem("1", "Keyboard", 5, 20, "Electronics")

        self.manager.add_item(item1)
        result = self.manager.add_item(item2)

        self.assertFalse(result)
        self.assertEqual(len(self.manager._items), 1)

    def test_remove_item(self):
        item = InventoryItem("1", "Mouse", 10, 15, "Electronics")
        self.manager.add_item(item)

        result = self.manager.remove_item("1")

        self.assertTrue(result)
        self.assertEqual(len(self.manager._items), 0)

    def test_save_and_load(self):
        item = InventoryItem("1", "Mouse", 10, 15, "Electronics")
        self.manager.add_item(item)

        self.manager.save_to_csv(self.test_file)

        InventoryManager._instance = None
        new_manager = InventoryManager()
        new_manager.load_from_csv(self.test_file)

        self.assertEqual(len(new_manager._items), 1)
        self.assertIsNotNone(new_manager.find_item_by_id("1"))

    def test_find_item_by_id(self):
        item = InventoryItem("1", "Mouse", 10, 15, "Electronics")
        self.manager.add_item(item)

        found_item = self.manager.find_item_by_id("1")

        self.assertIsNotNone(found_item)
        self.assertEqual(found_item._name, "Mouse")

    def test_find_item_by_name(self):
        item = InventoryItem("1", "Mouse", 10, 15, "Electronics")
        self.manager.add_item(item)

        found_item = self.manager.find_item_by_name("Mouse")

        self.assertIsNotNone(found_item)
        self.assertEqual(found_item._item_id, "1")

    def test_update_quantity(self):
        item = InventoryItem("1", "Mouse", 10, 15, "Electronics")
        self.manager.add_item(item)

        result = self.manager.update_quantity("1", 25)

        self.assertTrue(result)
        self.assertEqual(self.manager.find_item_by_id("1")._quantity, 25)

if __name__ == "__main__":
    unittest.main()