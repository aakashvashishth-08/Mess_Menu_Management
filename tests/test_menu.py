"""
Simple tests for the Mess Menu Manager.
Run from the project folder with:  python -m unittest discover
"""

import json
import os
import sys
import tempfile
import unittest

# Make sure the project folder is importable, even if tests are run from elsewhere
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import menu_manager
import validators


class TestValidation(unittest.TestCase):
    def test_valid_day(self):
        self.assertTrue(validators.is_valid_day("Monday"))
        self.assertTrue(validators.is_valid_day("  sunday "))

    def test_invalid_day(self):
        self.assertFalse(validators.is_valid_day("Funday"))
        self.assertFalse(validators.is_valid_day(""))

    def test_valid_and_invalid_meal(self):
        self.assertTrue(validators.is_valid_meal("lunch"))
        self.assertFalse(validators.is_valid_meal("Brunch"))

    def test_empty_item_not_allowed(self):
        self.assertFalse(validators.is_valid_item("   "))
        self.assertTrue(validators.is_valid_item("Rajma"))

    def test_menu_choice(self):
        self.assertEqual(validators.get_menu_choice("5", 1, 11), 5)
        self.assertIsNone(validators.get_menu_choice("abc", 1, 11))
        self.assertIsNone(validators.get_menu_choice("12", 1, 11))


class TestCrud(unittest.TestCase):
    def setUp(self):
        self.menu = menu_manager.get_default_menu()

    def test_add_item(self):
        done, message = menu_manager.add_item(self.menu, "Monday", "Lunch", "Rajma")
        self.assertTrue(done)
        self.assertIn("Rajma", self.menu["Monday"]["Lunch"])

    def test_add_duplicate_item(self):
        done, message = menu_manager.add_item(self.menu, "Monday", "Lunch", "dal")
        self.assertFalse(done)

    def test_edit_item(self):
        done, message = menu_manager.edit_item(self.menu, "Monday", "Lunch", "Dal", "Chole")
        self.assertTrue(done)
        self.assertIn("Chole", self.menu["Monday"]["Lunch"])
        self.assertNotIn("Dal", self.menu["Monday"]["Lunch"])

    def test_edit_missing_item(self):
        done, message = menu_manager.edit_item(self.menu, "Monday", "Lunch", "Pizza", "Chole")
        self.assertFalse(done)

    def test_delete_item(self):
        done, message = menu_manager.delete_item(self.menu, "Monday", "Breakfast", "Poha")
        self.assertTrue(done)
        self.assertNotIn("Poha", self.menu["Monday"]["Breakfast"])

    def test_delete_missing_item(self):
        done, message = menu_manager.delete_item(self.menu, "Monday", "Breakfast", "Pizza")
        self.assertFalse(done)

    def test_search_is_case_insensitive(self):
        results = menu_manager.search_item(self.menu, "paneer")
        self.assertIn(("Monday", "Dinner", "Paneer"), results)
        self.assertIn(("Thursday", "Dinner", "Paneer Masala"), results)

    def test_search_no_result(self):
        self.assertEqual(menu_manager.search_item(self.menu, "pizza"), [])


class TestFileHandling(unittest.TestCase):
    def setUp(self):
        self.folder = tempfile.TemporaryDirectory()
        self.path = os.path.join(self.folder.name, "menu.json")

    def tearDown(self):
        self.folder.cleanup()

    def test_save_and_load(self):
        menu = menu_manager.get_default_menu()
        menu["Monday"]["Lunch"].append("Rajma")
        menu_manager.save_menu(menu, self.path)
        loaded = menu_manager.load_menu(self.path)
        self.assertEqual(loaded, menu)

    def test_missing_file_gives_default_menu(self):
        loaded = menu_manager.load_menu(self.path)
        self.assertEqual(loaded, menu_manager.get_default_menu())

    def test_corrupted_file_gives_default_menu(self):
        with open(self.path, "w") as file:
            file.write("{ this is not valid json")
        loaded = menu_manager.load_menu(self.path)
        self.assertEqual(loaded, menu_manager.get_default_menu())

    def test_wrong_structure_gives_default_menu(self):
        with open(self.path, "w") as file:
            json.dump({"Monday": "no meals here"}, file)
        loaded = menu_manager.load_menu(self.path)
        self.assertEqual(loaded, menu_manager.get_default_menu())

    def test_reset_menu(self):
        menu_manager.save_menu({"Monday": {}}, self.path)
        menu = menu_manager.reset_menu(self.path)
        self.assertEqual(menu, menu_manager.get_default_menu())


if __name__ == "__main__":
    unittest.main()
