from src.task_tracker.cli import display_menu, get_user_choice
from src.task_tracker.config import MENU_OPTIONS 

def main():
    """Main loop for the Smart Task Tracker CLI."""
    while True:
        display_menu()
        choice = get_user_choice()

        if choice == "1":
            print("📝 Add Task feature coming soon!")
        elif choice == "2":
            print("📋 View Tasks feature coming soon!")
        elif choice == "3":
            print("❌ Delete Task feature coming soon!")
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid option. Please try again.")

if __name__ == "__main__":
    main()
# run this files only if its being run directly, not if its being imported elsewhere 