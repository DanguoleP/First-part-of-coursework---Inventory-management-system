import unittest
from models.item import InventoryItem
from models.manager import InventoryManager

class TestManager(unittest.TestCase):

    def test_add_item(self):
        manager = InventoryManager()
        manager._items.clear()

        item = InventoryItem("1", "Mouse", 10, 15, "Electronics")
        manager.add_item(item)

        self.assertEqual(len(manager._items), 1)

if __name__ == "__main__":
    unittest.main()