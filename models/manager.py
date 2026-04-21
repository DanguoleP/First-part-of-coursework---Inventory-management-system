import csv
import os
from models.item import InventoryItem

class InventoryManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._items = []
        return cls._instance

    def add_item(self, item):
        if self.find_item_by_id(item._item_id) is None:
            self._items.append(item)
            return True
        return False

    def remove_item(self, item_id):
        for item in self._items:
            if item._item_id == item_id:
                self._items.remove(item)
                return True
        return False

    def find_item_by_id(self, item_id):
        for item in self._items:
            if item._item_id == item_id:
                return item
        return None

    def find_item_by_name(self, name):
        for item in self._items:
            if item._name.lower() == name.lower():
                return item
        return None

    def update_quantity(self, item_id, new_quantity):
        item = self.find_item_by_id(item_id)
        if item is not None:
            item._quantity = new_quantity
            return True
        return False

    def print_items(self):
        if not self._items:
            print("Inventory empty.")
        for item in self._items:
            print(item.get_info())

    def save_to_csv(self, filename):
        try:
            os.makedirs(os.path.dirname(filename), exist_ok=True)

            with open(filename, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["id", "name", "quantity", "price", "category"])

                for item in self._items:
                    writer.writerow([
                        item._item_id,
                        item._name,
                        item._quantity,
                        item._price,
                        item._category
                    ])
        except Exception as e:
            print("Error saving file:", e)

    def load_from_csv(self, filename):
        try:
            self._items.clear()

            if not os.path.exists(filename):
                print("No existing inventory found")
                return

            with open(filename, "r") as f:
                reader = csv.DictReader(f)

                for row in reader:
                    item = InventoryItem(
                        row["id"],
                        row["name"],
                        int(row["quantity"]),
                        float(row["price"]),
                        row["category"]
                    )
                    self._items.append(item)

        except FileNotFoundError:
            print("File not found.")
        except Exception as e:
            print("Error loading file:", e)