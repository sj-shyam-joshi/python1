class GroceryList:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"Added {item} to the list.")

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f"Removed {item} from the list.")
        else:
            print(f"{item} not found in the list.")

    def view_list(self):
        if self.items:
            print("Grocery List:")
            for item in self.items:
                print(f"- {item}")
        else:
            print("Your grocery list is empty.")

    def mark_as_purchased(self, item):
        if item in self.items:
            print(f"Marked {item} as purchased.")
            self.items.remove(item)
        else:
            print(f"{item} not found in the list.")

def main():
    grocery_list = GroceryList()
    while True:
        print("\n1. Add item to list")
        print("2. Remove item from list")
        print("3. View list")
        print("4. Mark item as purchased")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            item = input("Enter the item to add: ")
            grocery_list.add_item(item)
        elif choice == "2":
            item = input("Enter the item to remove: ")
            grocery_list.remove_item(item)
        elif choice == "3":
            grocery_list.view_list()
        elif choice == "4":
            item = input("Enter the item to mark as purchased: ")
            grocery_list.mark_as_purchased(item)
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
