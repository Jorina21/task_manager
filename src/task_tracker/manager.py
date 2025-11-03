#src/task_tracker/manager.py

from datetime import datetime
from rich.console import Console 
from rich.table import Table 

console = Console()

class TaskManager:
    "Handles in-memory task storage and operations."
    def __init__(self):
        self.tasks = []

    def add_tasks(self, title, caterogy, due_date, priority):
        "add a new task to the list."
        try:
            due_date_obj = datetime.strptime(due_date, "%Y-%m-%d")
        except ValueError:
            console.print("[red]❌ Invalid date format. Use YYYY-MM-DD.[/red]")
            return

        task = {
            "title": title,
            "category": category,
            "due_date": due_date_obj,
            "priority" : priority,
            "completed" : False
        }
        
        self.tasks.append(task)
        console.print(f"[green]✅ Task '{title}' added successfully![/green]")

    def view_tasks(self):
        """Display all tasks in a table """
        if not self.tasks:
            console.print("[yellow]No tasks available yet![/yellow]")
            return

        table = Table(title = "your Tasks", title_style = "bold cyan")
        table.add_column("No", justify = "right", style "bold white")
        table.add_column("Title", style = "bold cyan")
        table.add_column("Category", style = "bold yellow")
        table.add_column("Due Date", style="bold magenta")
        table.add_column("Priority", style="bold green")
        table.add_column("Status", style="bold red")

        for i, t in enumerate(self.tasks, start = 1):
            status = "✅ Done" if t["completed"] else "⏳ Pending"
            table.add_row(
                str(i),
                t["title"],
                t["category"],
                t["due_date"].strftime("%Y-%m-%d"),
                t["priority"].capitalize(),
                status    

            )
            console.print(table)