#src/task_tracker/cli.py
from src.task_tracker.config import MENU_OPTIONS  
# you can import function using the dile and function name 

def display_menu():
    """Display the main menu options."""
    print("\n=== SMART TASK TRACKER ===")
    for key, option in MENU_OPTIONS.items():
        print(f"{key}. {option}")
    print()

def get_user_choice():
    """Prompt the user for a menu choice."""
    choice = input("Select an option: ").strip()
    return choice

