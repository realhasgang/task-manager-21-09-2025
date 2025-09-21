import os

TASKS_FILE = "tasks.txt"

def load_tasks():
    """Load tasks from file if available"""
    tasks = []
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            tasks = [line.strip() for line in f.readlines()]
    return tasks

def save_tasks(tasks):
    """Save tasks to file"""
    with open(TASKS_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def show_menu():
    print("\n==== Task Manager ====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks found.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task(tasks):
    task = input("\nEnter new task: ").strip()
    if task:
        tasks.append(task)
        print("✅ Task added successfully!")
    else:
        print("⚠️ Empty task not allowed.")

def delete_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            choice = int(input("\nEnter task number to delete: "))
            if 1 <= choice <= len(tasks):
                removed = tasks.pop(choice - 1)
                print(f"🗑️ Deleted: {removed}")
            else:
                print("⚠️ Invalid number.")
        except ValueError:
            print("⚠️ Please enter a valid number.")

def main():
    tasks = load_tasks()
    while True:
        show_menu()
        choice = input("\nEnter choice (1-4): ").strip()
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
            save_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
            save_tasks(tasks)
        elif choice == "4":
            save_tasks(tasks)
            print("\n👋 Goodbye! Your tasks are saved.")
            break
        else:
            print("⚠️ Invalid choice, try again.")

if __name__ == "__main__":
    main()
