import json
import os

# Load tasks from file
def load_tasks(filename='todo_data.json'):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return json.load(f)
    return []

# Save tasks to file
def save_tasks(tasks, filename='todo_data.json'):
    with open(filename, 'w') as f:
        json.dump(tasks, f, indent=4)

# Display tasks
def display_tasks(tasks):
    if not tasks:
        print("\nNo tasks found.\n")
        return

    print("\nTo-Do List:")
    for i, task in enumerate(tasks, start=1):
        status = '✔️' if task['completed'] else '❌'
        print(f"{i}. {task['title']} [{status}]")
    print()

# Add a new task
def add_task(tasks):
    title = input("\nEnter the task: ")
    tasks.append({'title': title, 'completed': False})
    save_tasks(tasks)
    print(f"Task '{title}' added successfully!\n")

# Edit an existing task
def edit_task(tasks):
    display_tasks(tasks)
    task_number = int(input("Enter the number of the task to edit: "))

    if 1 <= task_number <= len(tasks):
        new_title = input(f"Enter the new title for task '{tasks[task_number - 1]['title']}': ")
        tasks[task_number - 1]['title'] = new_title
        save_tasks(tasks)
        print(f"Task '{task_number}' updated to '{new_title}'!\n")
    else:
        print("Invalid task number.\n")

# Mark a task as completed
def complete_task(tasks):
    display_tasks(tasks)
    task_number = int(input("Enter the number of the task to mark as completed: "))
    
    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1]['completed'] = True
        save_tasks(tasks)
        print(f"Task '{tasks[task_number - 1]['title']}' marked as completed!\n")
    else:
        print("Invalid task number.\n")

# Delete a task
def delete_task(tasks):
    display_tasks(tasks)
    task_number = int(input("Enter the number of the task to delete: "))
    
    if 1 <= task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        save_tasks(tasks)
        print(f"Task '{removed_task['title']}' deleted successfully!\n")
    else:
        print("Invalid task number.\n")

# Main loop
def main():
    tasks = load_tasks()
    
    while True:
        print("\nTo-Do List Menu:")
        print("1. View To-Do List")
        print("2. Add Task")
        print("3. Edit Task")
        print("4. Mark Task as Completed")
        print("5. Delete Task")
        print("6. Exit")
        
        choice = input("\nChoose an option (1-6): ")
        
        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            edit_task(tasks)
        elif choice == '4':
            complete_task(tasks)
        elif choice == '5':
            delete_task(tasks)
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please choose again.\n")

if _name_ == '_main_':
    main()