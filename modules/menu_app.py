from datetime import datetime
from modules.config import MESS_NAMES, MEALS, DAYS
from modules.menu import get_menu
from modules.display import show_menu
from modules.input_helper import choose, pause

def browse_menu():
    mess = choose(MESS_NAMES, "Select mess:")
    day = choose(DAYS, "Select day:")
    meal = choose(MEALS, "Select meal:")
    show_menu(mess, day, meal, get_menu(mess, day, meal))
    pause()

def today_menu():
    mess = choose(MESS_NAMES, "Select mess:")
    day = datetime.now().strftime("%A")
    meal = choose(MEALS, "Select meal:")
    show_menu(mess, day, meal, get_menu(mess, day, meal))
    pause()

def run():
    while True:
        print("\n" + "=" * 40)
        print("VIT BHOPAL HOSTEL MESS")
        print("=" * 40)
        print("1. Browse Menu")
        print("2. Today's Menu")
        print("3. Exit")
        print("=" * 40)
        choice = input("Enter choice: ").strip()
        if choice == "1":
            browse_menu()
        elif choice == "2":
            today_menu()
        elif choice == "3":
            print("\nThank you for using the Mess Menu.")
            break
        else:
            print("Please enter a valid choice.")
