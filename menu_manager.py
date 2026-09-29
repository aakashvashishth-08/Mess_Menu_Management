import json
import os

DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
MEALS = ["Breakfast", "Lunch", "Snacks", "Dinner"]
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "data", "menu.json")


def get_default_menu():
    return {
        "Monday": {
            "Breakfast": ["Poha", "Tea"],
            "Lunch": ["Dal", "Rice", "Roti", "Aloo Sabzi"],
            "Snacks": ["Samosa", "Tea"],
            "Dinner": ["Paneer", "Roti", "Rice"],
        },
        "Tuesday": {
            "Breakfast": ["Aloo Paratha", "Curd"],
            "Lunch": ["Rajma", "Rice", "Roti", "Salad"],
            "Snacks": ["Biscuits", "Tea"],
            "Dinner": ["Mix Veg", "Dal", "Roti"],
        },
        "Wednesday": {
            "Breakfast": ["Idli", "Sambar"],
            "Lunch": ["Chole", "Rice", "Roti"],
            "Snacks": ["Sandwich", "Tea"],
            "Dinner": ["Dal Makhani", "Rice", "Roti"],
        },
        "Thursday": {
            "Breakfast": ["Poha", "Tea"],
            "Lunch": ["Kadhi", "Rice", "Roti"],
            "Snacks": ["Samosa", "Tea"],
            "Dinner": ["Paneer Masala", "Roti", "Rice"],
        },
        "Friday": {
            "Breakfast": ["Paratha", "Curd"],
            "Lunch": ["Dal", "Rice", "Roti", "Sabzi"],
            "Snacks": ["Maggi", "Tea"],
            "Dinner": ["Chole", "Bhature"],
        },
        "Saturday": {
            "Breakfast": ["Bread", "Butter", "Tea"],
            "Lunch": ["Rajma", "Rice", "Roti"],
            "Snacks": ["Pakora", "Tea"],
            "Dinner": ["Veg Biryani", "Raita"],
        },
        "Sunday": {
            "Breakfast": ["Puri", "Aloo Sabzi"],
            "Lunch": ["Special Thali"],
            "Snacks": ["Cake", "Juice"],
            "Dinner": ["Fried Rice", "Manchurian"],
        },
    }


def is_menu_structure_valid(menu):
    if not isinstance(menu, dict):
        return False
    for day in DAYS:
        if day not in menu or not isinstance(menu[day], dict):
            return False
        for meal in MEALS:
            if meal not in menu[day] or not isinstance(menu[day][meal], list):
                return False
            for item in menu[day][meal]:
                if not isinstance(item, str):
                    return False
    return True


def save_menu(menu, file_path=DATA_FILE):
    try:
        folder = os.path.dirname(file_path)
        if folder and not os.path.exists(folder):
            os.makedirs(folder)
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(menu, file, indent=4)
        return True
    except OSError:
        print("Error: could not save the menu file.")
        return False

def load_menu(file_path=DATA_FILE):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            menu = json.load(file)
    except FileNotFoundError:
        print("Menu file not found. Creating one with the default menu.")
        menu = get_default_menu()
        save_menu(menu, file_path)
        return menu
    except json.JSONDecodeError:
        print("Menu file is corrupted. Loading the default menu instead.")
        return get_default_menu()
    except OSError:
        print("Could not read the menu file. Loading the default menu instead.")
        return get_default_menu()

    if not is_menu_structure_valid(menu):
        print("Menu file has wrong data. Loading the default menu instead.")
        return get_default_menu()
    return menu


def reset_menu(file_path=DATA_FILE):
    menu = get_default_menu()
    save_menu(menu, file_path)
    return menu


def find_item_index(items, name):
    for index in range(len(items)):
        if items[index].lower() == name.lower():
            return index
    return -1


def add_item(menu, day, meal, item):
    items = menu[day][meal]
    if find_item_index(items, item) != -1:
        return False, item + " is already in " + day + " " + meal + "."
    items.append(item)
    return True, item + " added to " + day + " " + meal + "."


def edit_item(menu, day, meal, old_item, new_item):
    items = menu[day][meal]
    position = find_item_index(items, old_item)
    if position == -1:
        return False, old_item + " was not found in " + day + " " + meal + "."
    other = find_item_index(items, new_item)
    if other != -1 and other != position:
        return False, new_item + " is already in " + day + " " + meal + "."

    items[position] = new_item
    return True, old_item + " changed to " + new_item + "."


def delete_item(menu, day, meal, item):
    items = menu[day][meal]
    position = find_item_index(items, item)
    if position == -1:
        return False, item + " was not found in " + day + " " + meal + "."
    removed = items.pop(position)
    return True, removed + " deleted from " + day + " " + meal + "."


def search_item(menu, keyword):
    results = []
    keyword = keyword.lower()
    for day in DAYS:
        for meal in MEALS:
            for item in menu[day][meal]:
                if keyword in item.lower():
                    results.append((day, meal, item))
    return results
