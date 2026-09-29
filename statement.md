# Project Statement

## Problem Statement

In most hostels the weekly mess menu lives in a few different places: a notice on the wall, a message in a WhatsApp group, or a page in the warden's notebook. When the mess changes a dish, someone has to update all of these by hand, and students often end up looking at an old version. Checking what is being served, or finding which days have a particular dish, takes more effort than it should.

The Mess Menu Manager keeps the whole weekly menu in one place and lets the administrator view, change and search it from a simple command-line program.

## Scope of the Project

**The system can:**
- Manage a weekly menu (7 days, 4 meals per day)
- View the full week, one day, today, or one meal across the week
- Add, edit and remove food items
- Search for a food item
- Save the menu locally in a JSON file and load it again on the next run
- Reset the menu to a default weekly menu

**The system does not include:**
- Online food ordering
- Payment
- Student attendance
- Online authentication or user accounts
- Cloud hosting or a database server

## Target Users

- **Mess administrator** – maintains the menu (main user)
- **Hostel students** – check what is being served
- **Mess staff** – use the menu to plan cooking

## Objectives

1. Store the weekly mess menu in a single, organised structure.
2. Let the administrator add, edit and delete food items without editing files by hand.
3. Let anyone quickly view the menu by day, by meal, or for today.
4. Make it easy to find which days a particular dish is served.
5. Keep the data safe between runs by saving it in a JSON file.
6. Stop wrong input (bad day, empty item, etc.) from crashing the program.

## High-Level Features

- View weekly menu
- View menu for a chosen day
- View today's menu (day found automatically)
- View a meal (Breakfast / Lunch / Snacks / Dinner) for all days
- Add, edit and delete menu items
- Case-insensitive, partial-match search
- Reset to default menu (with confirmation)
- Save and load menu using JSON
- Input validation and error messages
- Safe exit (menu is saved on exit)