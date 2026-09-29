"""
main.py
Starts the Mess Menu Manager and runs the main menu loop.
Run with:  python main.py
"""

import menu_display
import menu_manager
import validators


def show_main_menu():
    menu_display.print_title("MESS MENU MANAGER")
    print("1. View Weekly Menu")
    print("2. View Menu for a Day")
    print("3. View Today's Menu")
    print("4. View Menu by Meal")
    print("5. Add Menu Item")
    print("6. Edit Menu Item")
    print("7. Delete Menu Item")
    print("8. Search Menu")
    print("9. Reset Default Menu")
    print("10. Save Menu")
    print("11. Exit")
    print()


def view_day(menu):
    day = validators.ask_day()
    if day is not None:
        menu_display.show_day(menu, day)


def view_meal(menu):
    meal = validators.ask_meal()
    if meal is not None:
        menu_display.show_meal_menu(menu, meal)


def add_menu_item(menu):
    day = validators.ask_day()
    if day is None:
        return
    meal = validators.ask_meal()
    if meal is None:
        return
    item = validators.ask_item("Enter food item")
    if item is None:
        return

    done, message = menu_manager.add_item(menu, day, meal, item)
    print(message)
    if done:
        menu_manager.save_menu(menu)  # keep the file up to date


def edit_menu_item(menu):
    day = validators.ask_day()
    if day is None:
        return
    meal = validators.ask_meal()
    if meal is None:
        return
    menu_display.show_day(menu, day)
    old_item = validators.ask_item("Enter old item")
    if old_item is None:
        return
    new_item = validators.ask_item("Enter new item")
    if new_item is None:
        return

    done, message = menu_manager.edit_item(menu, day, meal, old_item, new_item)
    print(message)
    if done:
        menu_manager.save_menu(menu)


def delete_menu_item(menu):
    day = validators.ask_day()
    if day is None:
        return
    meal = validators.ask_meal()
    if meal is None:
        return
    menu_display.show_day(menu, day)
    item = validators.ask_item("Enter item to delete")
    if item is None:
        return

    done, message = menu_manager.delete_item(menu, day, meal, item)
    print(message)
    if done:
        menu_manager.save_menu(menu)


def search_menu(menu):
    keyword = input("Search food item: ").strip()
    if not validators.is_valid_item(keyword):
        print("Search text cannot be empty.")
        return
    results = menu_manager.search_item(menu, keyword)
    menu_display.show_search_results(results, keyword)


def reset_menu(menu):
    """Reset only after the user confirms. Returns the menu to use."""
    if validators.ask_yes_no("Are you sure you want to reset the menu? (yes/no): "):
        print("Menu reset to the default weekly menu.")
        return menu_manager.reset_menu()
    print("Reset cancelled.")
    return menu


def main():
    menu = menu_manager.load_menu()  # load the saved menu when the program starts

    while True:
        show_main_menu()
        choice = validators.get_menu_choice(input("Enter your choice: "), 1, 11)

        if choice is None:
            continue
        elif choice == 1:
            menu_display.show_weekly_menu(menu)
        elif choice == 2:
            view_day(menu)
        elif choice == 3:
            menu_display.show_today_menu(menu)
        elif choice == 4:
            view_meal(menu)
        elif choice == 5:
            add_menu_item(menu)
        elif choice == 6:
            edit_menu_item(menu)
        elif choice == 7:
            delete_menu_item(menu)
        elif choice == 8:
            search_menu(menu)
        elif choice == 9:
            menu = reset_menu(menu)
        elif choice == 10:
            if menu_manager.save_menu(menu):
                print("Menu saved successfully.")
        elif choice == 11:
            menu_manager.save_menu(menu)
            print("Menu saved. Goodbye!")
            break

        menu_display.pause()


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        # Ctrl+C or closed input: exit without a scary error message
        print("\nProgram closed.")
