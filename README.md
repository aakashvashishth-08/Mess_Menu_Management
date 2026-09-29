# Mess Menu Manager

## 1. Project Overview

Mess Menu Manager is a simple Python-based project made for managing the weekly menu of a college mess.

In a college mess, the food menu is usually shared through notices, messages or other manual methods. This project provides a simple way to store and manage the menu from one place, Manager can edit, add and delete food items from the menu.


## 2. Main Features

1. View the complete weekly menu.
2. View the menu for a particular day.
3. View today's menu automatically.
4. View menus according to meal type.
5. Add a new food item.
6. Edit an existing food item.
7. Delete a food item.
8. Search for a food item in the weekly menu.
9. Reset the menu to the default menu.
10. Save menu changes.
11. Load the saved menu when the program starts.
12. Handle invalid inputs without closing the program.


## 3. How to Run the Project

1. Clone your repository

```bash
git clone https://github.com/aakashvashishth-08/Mess_Menu_Management.git
```

2. Enter the project folder

```bash
cd Mess_Menu_Management
```
3.Run the main program

```bash
python main.py
```


##4. Use the Main Menu

After starting the program, a menu will appear similar to:

```text
========================================
          MESS MENU MANAGER
========================================

1. View Weekly Menu
2. View Day Menu
3. Today's Menu
4. View by Meal
5. Add Menu Item
6. Edit Menu Item
7. Delete Menu Item
8. Search Menu
9. Reset Menu
10. Save Menu
11. Exit

Enter your choice:
```


## 5. How the Menu Data is Stored

The menu is stored in:

```text
data/menu.json
```

## 6. Adding a Menu Item

To add food, select the Add Menu Item option.

The program asks for:

1. Day
2. Meal
3. Food item

For example:

```text
Enter day: Monday
Enter meal: Lunch
Enter food item: Rajma
```

The new item is then added to the selected meal.

## 7. Editing a Menu Item

The Edit Menu Item option can be used when a food item needs to be changed.

For example:

```text
Enter day: Monday
Enter meal: Lunch
Enter old item: Rajma
Enter new item: Chole
```

## 8. Deleting a Menu Item

The Delete Menu Item option removes an item from a particular meal. The program asks for the day, meal and food item that needs to be removed. The user is also given a message if the item does not exist.


## 9. Topics Learned

During this project, the following Python concepts are used:

1. Variables and data types were used for storing information.
2. Lists were used for storing multiple food items.
3. Dictionaries were used for organizing days and meals.
4. Conditional statements were used for making decisions.
5. Loops were used for repeatedly displaying and processing data.
6. Functions were used to divide the program into smaller parts.
7. Modules were used to keep different parts of the project organized.
8. File handling was used to work with stored data.
9. JSON was used for saving the menu.
10. Exception handling was used to handle errors.
11. Searching was used to find food items in the menu.
12. The datetime module was used to find the current day.

## 10. Future Improvements

The current project is designed as a simple command-line application. Some possible improvements in the future are:

1. Adding a graphical user interface.
2. Adding student login and administrator login.
3. Adding a database instead of a JSON file.
4. Allowing students to give feedback about meals.
5. Adding a monthly menu.
6. Adding nutrition information for food items.
7. Adding an option to export the menu as a PDF.
8. Adding notifications when the menu is changed.


## 11. Conclusion

Mess Menu Manager is a small project that uses basic Python concepts to solve a practical problem in a college mess. It keeps the weekly menu organized and allows the user to make changes without editing the JSON file manually.

The main purpose of making this project was to understand how different Python concepts can be combined to create a complete working application rather than writing separate programs for each concept.
