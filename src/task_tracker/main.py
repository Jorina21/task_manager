
from rich.console import Console
from rich.panel import Panel 

from src.task_tracker.cli import display_menu, get_user_choice
from src.task_tracker.config import MENU_OPTIONS 

console = Console()

def main():
    """Main loop for the Smart Task Tracker CLI."""
    while True:
        display_menu()
        choice = get_user_choice()
        
        if choice == "1":
            console.print("[cyan]📝 Add Task feature coming soon![/cyan]")
            input("\nPress Enter to return to the menu...")
        elif choice == "2":
            console.print("[yellow]📋 View Tasks feature coming soon![/yellow]")
            input("\nPress Enter to return to the menu...")
        elif choice == "3":
            console.print("[red]❌ Delete Task feature coming soon![/red]")
            input("\nPress Enter to return to the menu...")
        elif choice == "4":
            console.print(Panel("[bold green]👋 Goodbye! Thanks for using Smart Task Tracker![/bold green]", expand=False))
            break
        else:
            console.print("[bold red]⚠️ Invalid option. Please try again.[/bold red]")
            input("\nPress Enter to return to the menu...")
        

if __name__ == "__main__":
    main()
# run this files only if its being run directly, not if its being imported elsewhere 