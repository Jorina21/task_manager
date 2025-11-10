#src/task_tracker/cli.py
from src.task_tracker.config import MENU_OPTIONS  
# you can import function using the dile and function name 
from src.task_tracker.manager import TaskManager

manager = TaskManager()

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


def handle_add_task():
    """Ask user for details and add a new task."""
    print("\n ---Add a New Task ---")
    title = input("Enter task title: ").strip()
    category = input("Enter category (work, study, Personal, etc.):").strip()
    due_date = input("Enter due date (YYYY-MM-DD): ").strip()
    priority = input("Enter priority (low, medium, high): ").strip()
    manager.add_task(title, category, due_date, priority)

def handle_view_tasks():
    """Display all task."""
    manager.view_tasks()


def handle_delete_task():
    """Ask user for a task to be deleted. """
    manager.view_tasks()
    if not manager.tasks:
        return
    
    try:
        num = int(input("Enter a valid number. "))
        manager.delete_task(num)
    except ValueError:
        print("Please enter a valid number.")


def handle_mark_complete():
    """ask user to a task number and mark it complete."""
    manager.view_tasks()
    
    if not manager.tasks:
        return
    
    try:
        num = int(input("Enter the task number to mark complete:"))
        manager.mark_task_completed(num)
    except ValueError:
        print("Please enter a valid number.")