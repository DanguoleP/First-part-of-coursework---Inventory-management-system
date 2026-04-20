from abc import ABC, abstractmethod

class BaseItem(ABC):
    def __init__(self, item_id, name, quantity, price):
        self._item_id = item_id
        self._name = name
        self._quantity = quantity
        self._price = price

    def add_stock(self, amount):
        self._quantity += amount

    def remove_stock(self, amount):
        if amount <= self._quantity:
            self._quantity -= amount
            return True
        return False

    @abstractmethod
    def get_info(self):
        pass

class InventoryItem(BaseItem):
    def __init__(self, item_id, name, quantity, price, category):
        super().__init__(item_id, name, quantity, price)
        self._category = category

    def get_info(self):
        return f"{self._name} ({self._category}) - {self._quantity} pcs - {self._price}€"