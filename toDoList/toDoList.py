todo_list = ["Buy groceries", "Clean house", "Walk dog"]

task_details = {
    "Buy groceries": {"priority": "High", "estimated_time": "1 hour"}, 
    "Clean house": {"priority": "Medium", "estimated_time": "2 hours"},
    "Walk dog": {"priority": "Low", "estimated_time": "30 minutes"}
}

for task in todo_list:
    print (f"Task: {task}")
    print(f"Priority: {task_details [task] ['priority']}")
    print(f"Estimated time: {task_details[task] ['estimated_time']}\n")
    