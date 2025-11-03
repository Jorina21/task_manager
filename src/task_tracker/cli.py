#src/task_tracker/cli.py

#using rich for better visuals 
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt
from src.task_tracker.config import MENU_OPTIONS  
# you can import function using the dile and function name 

console = Console()

# handles the user interface 
def display_menu():
    """Displays the main menu with rich styling."""
    console.clear()
    console.print(Panel.fit("[bold cyan]SMART TASK TRACKER[/bold cyan]", style="bold blue"))

    table = Table(title="Main Menu", title_style="bold magenta", header_style="bold white")
    table.add_column("Option", justify="center", style="bold green")
    table.add_column("Action", justify="left", style="white")

    for key, action in MENU_OPTIONS.items():
        table.add_row(key, action)

    console.print(table)
    console.print("[dim]Type the number of your choice and press Enter[/dim]\n")

def get_user_choice():
    """Prompts the user to choose an option."""
    choice = Prompt.ask("[bold yellow]Select an option[/bold yellow]").strip()
    return choice

