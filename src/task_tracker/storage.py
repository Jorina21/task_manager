#src/task_tracker/storage.py

import json 
from datetime import datetime 
from src.task_tracker.config import DATA_FILE, DATE_FORMAT

def load_task(): 
    """
    Load tasks from the JSON file in config.py
    Return a list of task dictionaries
    If the file doesnt exist or is invalid, returns a empty list.
    """

    try:
        with open(DATA_FILE, "r", encoding = "utf - 8") as f: 
            raw_data = json.load(f)

    except FileNotFoundError:
            # no file created --> start with empty task list 
            return []
        
    except json.JSONDecodeError:
            #file is corrupted or empty --> start fresh 
            print("Warning: tasks.json is not valid JSON. Starting with an empty task list")
            return[]



    tasks = [] 

    for item in raw_data: 
        try:
                due_date_str = item["due_date"]
                due_date_obj = datetime.strptime(due_date_str, DATE_FORMAT)
        
        except (keyError, ValueError):
                #skip tasks with invalid or missing dates 
                print(f"Warning: Skipping task with invalid date: {item}")
                continue


        task = {
                "title": item.get("title", ""),
                "category" : item.get("category", ""),
                "due_date" : due_date_obj,
                "priority" : item.get("priority", "medium"),
                "completed" : item.get("completed", False), 
            }
        tasks.append(task)

    return tasks


def save_tasks(tasks): 
    """
    Save the given list of task dictionalries to the json file
    Convert date time objects to string 
    """
    
    data_to_save = []

    for task in tasks: 
        #convert datetime to string so json accepts 
        due_date_str = task["due_date"].strftime(DATE_FORMAT)

        data_to_save.append({
            "title": task["title"],
            "category": task["category"],
            "due_date" : due_date_str,
            "priority" : task["priority"],
            "completed" : task["completed"],
        })

    with open(DATA_FILE, "w", encoding = "utf-8") as f:
        json.dump(data_to_save, f, indent = 2)
