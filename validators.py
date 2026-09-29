"""
validators.py
Checks the user's input and keeps asking until it is correct.
"""

from menu_manager import DAYS, MEALS


# ---------- Simple checks (used by the program and by the tests) ----------

def is_valid_day(day):
    """True if the text is one of the seven days (any capitalisation)."""
    return day.strip().capitalize() in DAYS


def is_valid_meal(meal):
    """True if the text is Breakfast, Lunch, Snacks or Dinner."""
    return meal.strip().capitalize() in MEALS


def is_valid_item(item):
    """A food item must not be empty."""
    return item.strip() != ""


def clean_item(item):
    """Remove extra spaces and capitalise each word, e.g. 'aloo  sabzi' -> 'Aloo Sabzi'."""
    return " ".join(item.split()).title()


def get_menu_choice(text, lowest, highest):
    """Turn the typed text into a number in range. Returns None if invalid."""
    try:
        choice = int(text.strip())
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None
    if choice < lowest or choice > highest:
        print("Invalid choice. Enter a number from " + str(lowest) + " to " + str(highest) + ".")
        return None
    return choice


# ---------- Functions that ask the user (loop until valid) ----------
# Typing "cancel" at any prompt returns None so the user can go back.

def ask_day():
    while True:
        text = input("Enter day (or 'cancel'): ").strip()
        if text.lower() == "cancel":
            return None
        if is_valid_day(text):
            return text.capitalize()
        print("Invalid day. Please enter a valid day.")


def ask_meal():
    while True:
        text = input("Enter meal (or 'cancel'): ").strip()
        if text.lower() == "cancel":
            return None
        if is_valid_meal(text):
            return text.capitalize()
        print("Invalid meal. Choose Breakfast, Lunch, Snacks or Dinner.")


def ask_item(prompt):
    while True:
        text = input(prompt + " (or 'cancel'): ")
        if text.strip().lower() == "cancel":
            return None
        if is_valid_item(text):
            return clean_item(text)
        print("Food item cannot be empty.")


def ask_yes_no(question):
    while True:
        answer = input(question).strip().lower()
        if answer == "yes" or answer == "y":
            return True
        if answer == "no" or answer == "n":
            return False
        print("Please type yes or no.")
