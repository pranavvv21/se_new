"""
A simple inventory management system to track stock levels.
"""
import json
from datetime import datetime


class Inventory:
    """Manages the inventory stock, including loading, saving, and modifying."""

    def __init__(self, stock_file="inventory.json"):
        """Initializes the inventory, loading data from the file."""
        self.stock_file = stock_file
        self.stock_data = {}
        self.load_data()

    def add_item(self, item="default", qty=0, logs=None):
        """Adds a specified quantity of an item to the stock."""
        if logs is None:
            logs = []

        if not isinstance(item, str) or not isinstance(qty, int):
            print(f"Error: Invalid item type '{type(item)}' or quantity type '{type(qty)}'.")
            return

        self.stock_data[item] = self.stock_data.get(item, 0) + qty
        logs.append(f"{str(datetime.now())}: Added {qty} of {item}")

    def remove_item(self, item, qty):
        """Removes a specified quantity of an item from the stock."""
        try:
            if self.stock_data[item] - qty <= 0:
                del self.stock_data[item]
                print(f"Info: '{item}' removed from stock.")
            else:
                self.stock_data[item] -= qty
        except KeyError:
            print(f"Info: Item '{item}' not in stock, nothing removed.")

    def get_qty(self, item):
        """Gets the current stock quantity for a given item."""
        return self.stock_data.get(item, 0)

    def load_data(self):
        """Loads the stock data from the JSON file."""
        try:
            with open(self.stock_file, "r", encoding="utf-8") as f:
                self.stock_data = json.loads(f.read())
        except FileNotFoundError:
            self.stock_data = {}
        except json.JSONDecodeError:
            print(f"Error: Could not decode {self.stock_file}. Starting empty.")
            self.stock_data = {}

    def save_data(self):
        """Saves the current stock data to the JSON file."""
        try:
            with open(self.stock_file, "w", encoding="utf-8") as f:
                f.write(json.dumps(self.stock_data, indent=4))
        except IOError as e:
            print(f"Error: Could not save data to {self.stock_file}. {e}")

    def print_data(self):
        """Prints a report of all items and their quantities."""
        print("\n--- Items Report ---")
        if not self.stock_data:
            print("Inventory is empty.")
        for item, qty in self.stock_data.items():
            print(f"{item} -> {qty}")
        print("--------------------\n")

    def check_low_items(self, threshold=5):
        """Returns a list of items with stock below the threshold."""
        return [item for item, qty in self.stock_data.items() if qty < threshold]


def main():
    """Main function to run the inventory operations."""
    inventory = Inventory()
    print("Initial data loaded.")
    inventory.print_data()

    inventory.add_item("apple", 10)
    inventory.add_item("banana", 8)

    inventory.add_item(123, 5)
    inventory.add_item("grapes", "ten")

    inventory.remove_item("apple", 3)
    inventory.remove_item("orange", 1)
    inventory.remove_item("banana", 10)

    print(f"Apple stock: {inventory.get_qty('apple')}")
    print(f"Banana stock: {inventory.get_qty('banana')}")

    print(f"Low items (below 5): {inventory.check_low_items()}")

    inventory.print_data()

    inventory.save_data()
    print("Final data saved.")


if __name__ == "__main__":
    main()