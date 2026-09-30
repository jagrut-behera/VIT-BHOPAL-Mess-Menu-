def show_menu(mess, day, meal, items):
    print("\n" + "=" * 40)
    print("VIT BHOPAL MESS MENU")
    print("=" * 40)
    print("Mess :", mess)
    print("Day  :", day)
    print("Meal :", meal)
    print("-" * 40)
    for item in items:
        print("-", item)
    print("=" * 40)
