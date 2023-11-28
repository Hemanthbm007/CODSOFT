import sys

tasks = []

def show_menu():
    print("To-Do List App")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as completed")
    print("4. Exit")
    print()

def add_task():
    task = input("Enter the task: ")
    tasks.append({"task": task, "completed": False})
    print("Task added successfully!")

def view_tasks():
    if not tasks:
        print("No tasks yet.")
    else:
        print("Tasks:")
        for idx, task in enumerate(tasks, start=1):
            status = "Completed" if task["completed"] else "Pending"
            print(f"{idx}. {task['task']} - {status}")

def mark_completed():
    view_tasks()
    task_idx = int(input("Enter the task number to mark as completed: ")) - 1
    if 0 <= task_idx < len(tasks):
        tasks[task_idx]["completed"] = True
        print("Task marked as completed!")
    else:
        print("Invalid task number.")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_completed()
        elif choice == "4":
            print("Exiting...")
            sys.exit(0)
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
