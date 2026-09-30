from modules.data import MENU

def get_menu(mess, day, meal):
    return MENU.get(mess, {}).get(day, {}).get(meal, [])
