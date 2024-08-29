import json
import os
TODO_FILE = 'todo_list.json'

def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TODO_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)
        
def display_tasks(tasks):
    if not tasks:
        print("No tasks to display.")
        return
    for idx, task in enumerate(tasks):
        status = "Done" if task['completed'] else "Not Done"
        print(f"{idx + 1}. {task['description']} - {status}")
        
def add_task(tasks):
    description = input("Enter task description: ")
    tasks.append({'description': description, 'completed': False})
    save_tasks(tasks)
    print("Task added successfully.")
    
def update_task(tasks):
    display_tasks(tasks)
    try:
        task_id = int(input("Enter task number to update: ")) - 1
        if 0 <= task_id < len(tasks):
            new_description = input("Enter new description: ")
            tasks[task_id]['description'] = new_description
            save_tasks(tasks)
            print("Task updated successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")
        
def delete_task(tasks):
    display_tasks(tasks)
    try:
        task_id = int(input("Enter task number to delete: ")) - 1
        if 0 <= task_id < len(tasks):
            tasks.pop(task_id)
            save_tasks(tasks)
            print("Task deleted successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")
        
def mark_completed(tasks):
    display_tasks(tasks)
    try:
        task_id = int(input("Enter task number to mark as completed: ")) - 1
        if 0 <= task_id < len(tasks):
            tasks[task_id]['completed'] = True
            save_tasks(tasks)
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")
        
def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List Application")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task as Completed")
        print("6. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            update_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            mark_completed(tasks)
        elif choice == '6':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
