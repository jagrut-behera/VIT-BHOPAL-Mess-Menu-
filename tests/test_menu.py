import unittest
from modules.menu import get_menu

class TestMenu(unittest.TestCase):
    def test_menu(self):
        items = get_menu("Mayuri Boys Mess", "Monday", "Breakfast")
        self.assertIn("Poha", items)

    def test_second_mess(self):
        items = get_menu("JMB Boys Mess", "Sunday", "Dinner")
        self.assertIn("Veg Biryani", items)

    def test_missing_menu(self):
        self.assertEqual(get_menu("Mayuri Boys Mess", "Monday", "Snacks"), [])

if __name__ == "__main__":
    unittest.main()
