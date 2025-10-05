# Student name : Abdulaziz Mohammed Alkhlaiwe
# Student ID: 444101708

"""Write a program that builds a simple inventory system using a dictionary where:
- Key = product name, Value = quantity in stock.
- The user can repeatedly choose one of the following actions:
1. Add a new product.
2. Update quantity.
3. Display all products.
4. Exit.
Use a while True loop and if/elif statements for the menu options.
Concepts: dictionaries, loops, conditional branching, data storage.
"""


def display_menu():
    print("\n=== Inventory Menu ===")
    print("1. Add a new product")
    print("2. Update quantity")
    print("3. Display all products")
    print("4. Exit")

def main():
    inventory = {}  # dict[str, int]

    while True:
        display_menu()
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            name = input("Enter product name: ").strip()
            if not name:
                print("Product name cannot be empty.")
                continue
            if name in inventory:
                print("Product already exists. Use option 2 to update quantity.")
                continue
            try:
                qty = int(input("Enter initial quantity (integer): "))
                if qty < 0:
                    raise ValueError("Quantity cannot be negative.")
            except ValueError as e:
                print(f"Invalid quantity: {e}")
                continue
            inventory[name] = qty
            print(f"Added '{name}' with quantity {qty}.")

        elif choice == "2":
            name = input("Enter product name to update: ").strip()
            if name not in inventory:
                print("Product not found.")
                continue
            try:
                qty = int(input("Enter new quantity (integer): "))
                if qty < 0:
                    raise ValueError("Quantity cannot be negative.")
            except ValueError as e:
                print(f"Invalid quantity: {e}")
                continue
            inventory[name] = qty
            print(f"Updated '{name}' to quantity {qty}.")

        elif choice == "3":
            if not inventory:
                print("Inventory is empty.")
            else:
                print("\n--- All Products ---")
                for prod, qty in inventory.items():
                    print(f"- {prod}: {qty}")

        elif choice == "4":
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1-4.")

if __name__ == "__main__":
    main()
