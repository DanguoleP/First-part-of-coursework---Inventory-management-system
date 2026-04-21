from models.item import InventoryItem
from models.manager import InventoryManager

def menu():
    print("\n=== Inventory Management System ===")
    print("1 Add item")
    print("2 Remove item")
    print("3 Show inventory")
    print("4 Save inventory")
    print("5 Load inventory")
    print("6 Find item by ID")
    print("7 Find item by name")
    print("0 Exit")

def main():
    username = input("Enter your username: ").strip()
    if not username:
        print("Username cannot be empty.")
        return

    filename = f"data/{username}_inventory.csv"

    manager = InventoryManager()
    manager.load_from_csv(filename)

    print(f"Welcome, {username}!")

    while True:
        menu()
        choice = input("Choose a number to proceed: ")

        if choice == "1":
            item_id = input("ID: ")

            if manager.find_item_by_id(item_id):
                print("Item with this ID already exists.")
                continue

            name = input("Name: ")

            try:
                quantity = int(input("Quantity: "))
                price = float(input("Price: "))
            except ValueError:
                print("Invalid input. Quantity and price must be numbers.")
                continue

            if quantity < 0 or price < 0:
                print("Quantity and price cannot be negative.")
                continue

            category = input("Category: ")

            item = InventoryItem(item_id, name, quantity, price, category)

            if manager.add_item(item):
                print("Item added.")
            else:
                print("Item with this ID already exists.")

        elif choice == "2":
            item_id = input("Enter ID to remove: ")
            if manager.remove_item(item_id):
                print("Removed.")
            else:
                print("Not found.")

        elif choice == "3":
            manager.print_items()

        elif choice == "4":
            manager.save_to_csv(filename)
            print("Saved.")

        elif choice == "5":
            manager.load_from_csv(filename)
            print("Loaded.")

        elif choice == "6":
            item_id = input("Enter ID: ")
            item = manager.find_item_by_id(item_id)

            if item:
                print("Found:", item.get_info())
            else:
                print("Item not found.")

        elif choice == "7":
            name = input("Enter name: ")
            item = manager.find_item_by_name(name)

            if item:
                print("Found:", item.get_info())
            else:
                print("Item not found.")

        elif choice == "0":
            manager.save_to_csv(filename)
            print("Exiting program.")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()