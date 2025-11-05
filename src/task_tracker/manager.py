#src/task_tracker/manager.py 

from datetime import datetime

class TaskManager:
    """Handles in-memory taks storage and operations"""
    def __init__(self):
        self.tasks = []
    
    def add_task(self, title, catergory, due_date, priority):
        """Add a new task to the list""" 
        #try to partse the date to ensure correct format
        try:
            due_date_obj = datetime.strptime(due_date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD")
            return #cancels function call and goes back to the menu of choices.

        tasks = {
            "title" : title,
            "catergory" : catergory,
            "due_date" : due_date_obj,
            "priority" : priority,
            "completed" : False
        }

        self.tasks.append(task)
        print(f"Task '{title}' added succesfully!")

    
    def view_tasks(self):
        """Display all tasks in a simple table."""
        if not self.tasks:
            print("No taks available yet!")
            return

        print("\n --Your Tasks ---")
        print(f"{'No.':<5}{'Title':<25}{'Category':<15}{'Due Date':<12}{'Priority':<10}{'Status':<10}")
        print("-" * 80)

        for i, tasks in enumerate(self.tasks, start = 1):
            status = "Done" if task["completed"] else "Pending" #ternary expression (one line if statement)
            print(f"{i:<5}{task['title']:<25}{task['category']:<15}{task['due_date'].strftime('%Y-%m-%d'):<12}{task['priority']:<10}{status:<10}")