from src.task_tracker.cli import (display_menu,
 get_user_choice,
   handle_add_task,
    handle_view_tasks,
     handle_delete_task,
      handle_mark_complete,
)
#from src.task_tracker.config import MENU_OPTIONS

def main():
    #the main loop
    while True:
        display_menu()
        choice = get_user_choice()

        if choice == "1":
            #Add Task
            handle_add_task()
        elif choice == "2":
            #View Tasks 
            handle_view_tasks()
        elif choice == "3":
            # Delete Task 
            handle_delete_task()
        elif choice == "4":
            # mark complete
            handle_mark_complete()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

#main guard: only run this file if its being exucted indipendtely now when imported.
if __name__ == "__main__":
    main()