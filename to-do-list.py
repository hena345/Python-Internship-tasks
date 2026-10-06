# Task 2: To-Do List CLI App

tasks = []

def add_task():
    task = input("\nEnter task description: ").strip()
    if task:
        tasks.append(task)
        print(f"Added: '{task}'")
    else:
        print("Task cannot be blank.")

def view_tasks():
    if not tasks:
        print("\nNo tasks found.")
    else:
        print("\n=== Current Tasks ===")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

def remove_task():
    view_tasks()
    if not tasks:
        return
    try:
        num = int(input("\nEnter task number to remove: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f"Removed: '{removed}'")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def save_tasks():
    try:
        with open("tasks.txt", "w") as f:
            for task in tasks:
                f.write(f"{task}\n")
        print("Tasks saved to tasks.txt")
    except Exception as e:
        print(f"Error saving tasks: {e}")

def main():
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. View Tasks\n2. Add Task\n3. Remove Task\n4. Save & Exit")
        choice = input("Choose an option (1-4): ").strip()

        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            save_tasks()
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid selection.")

if __name__ == "__main__":
    main()
