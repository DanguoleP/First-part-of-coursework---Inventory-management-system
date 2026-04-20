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
        self._items.append(item)

    def remove_item(self, item_id):
        for item in self._items:
            if item._item_id == item_id:
                self._items.remove(item)
                return True
        return False

    def print_items(self):
        if not self._items:
            print("Inventory empty.")
        for item in self._items:
            print(item.get_info())

    def save_to_csv(self, filename):
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

    def load_from_csv(self, filename):
        self._items.clear()

        if not os.path.exists(filename):
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