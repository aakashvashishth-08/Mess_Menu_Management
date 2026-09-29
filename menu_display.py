import datetime

from menu_manager import DAYS, MEALS

LINE_WIDTH = 40


def print_line(character="-"):
    print(character * LINE_WIDTH)


def print_title(title):
    print()
    print_line("=")
    print(title.center(LINE_WIDTH))
    print_line("=")


def pause():
    input("\nPress Enter to return to the main menu...")


def get_today_name():
    today_number = datetime.date.today().weekday()
    return DAYS[today_number]


def format_items(items):
    if len(items) == 0:
        return "No items"
    return ", ".join(items)


def show_day(menu, day):
    print()
    print(day)
    print_line()
    for meal in MEALS:
        print(meal.ljust(10) + ": " + format_items(menu[day][meal]))


def show_weekly_menu(menu):
    print_title("WEEKLY MENU")
    for day in DAYS:
        show_day(menu, day)


def show_today_menu(menu):
    today = get_today_name()
    print_title("TODAY'S MENU")
    print("Today is " + today + ".")
    show_day(menu, today)


def show_meal_menu(menu, meal):
    print_title(meal.upper() + " MENU")
    for day in DAYS:
        print(day.ljust(10) + ": " + format_items(menu[day][meal]))


def show_search_results(results, keyword):
    if len(results) == 0:
        print("No matching food item found.")
        return
    print()
    print(keyword.title() + " found in:")
    for day, meal, item in results:
        print(day + " - " + meal + " (" + item + ")")
