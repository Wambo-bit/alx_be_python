# shopping_list_manager.py

def display_menu():
    def display_menu():
     print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []  # The array being tested

    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice (1-4): "))  # Ensure numeric input
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 4.")
            continue

        if choice == 1:
            item = inputinput("Enter the item to add: ")
            shopping_list.append(item)
            print(f"'{item}' added to the list.")
        elif choice == 2:
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' removed from the list.")
            else:
                print(f"'{item}' not found in the list.")
        elif choice == 3:
            if not shopping_list:
                print("Shopping list is empty.")
            else:
                print("Shopping List Manager")

                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()
