from models.item import InventoryItem
from models.manager import InventoryManager

def menu():
    print("\n=== Inventory Management System ===")
    print("1. Add item")
    print("2. Remove item")
    print("3. Show inventory")
    print("4. Save inventory")
    print("5. Load inventory")
    print("0. Exit")

def main():
    manager = InventoryManager()

    while True:
        menu()
        choice = input("Choose: ")

        if choice == "1":
            item_id = input("ID: ")
            name = input("Name: ")
            quantity = int(input("Quantity: "))
            price = float(input("Price: "))
            category = input("Category: ")

            item = InventoryItem(item_id, name, quantity, price, category)
            manager.add_item(item)
            print("Item added.")

        elif choice == "2":
            item_id = input("Enter ID to remove: ")
            if manager.remove_item(item_id):
                print("Removed.")
            else:
                print("Not found.")

        elif choice == "3":
            manager.print_items()

        elif choice == "4":
            manager.save_to_csv("data/inventory.csv")
            print("Saved.")

        elif choice == "5":
            manager.load_from_csv("data/inventory.csv")
            print("Loaded.")

        elif choice == "0":
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()