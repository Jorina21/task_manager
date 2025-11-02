# handles the user interface 

from src.task_tracker.config import MENU_OPTIONS  
# you can import function using the dile and function name 

def display_menu():
    """Prints the main menu options."""
    print("\n=== SMART TASK TRACKER ===")
    for key, option in MENU_OPTIONS.items():
        print(f"{key}.{option}")
    print() # space for spacing 

def get_user_choice():
    """Ask the user for a menu choice and return it. """

    choice = input("select an option: ").strip() #removes spaces strip()
    return choice 

