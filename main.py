from todo_list import ToDoList, Task


def display_tasks(tasks):
    """Utility function to display tasks."""
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")


def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Manager")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Completed")
        print("4. Edit Task")
        print("5. Filter Tasks by Status")
        print("6. Clear All Tasks")
        print("7. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            name = input("Enter task name: ")
            while True:
                priority = input("Enter task priority (Low, Normal, High): ").capitalize() or "Normal"
                if priority in Task.VALID_PRIORITIES:
                    break
                print(f"Invalid priority '{priority}'. Please enter one of: {', '.join(Task.VALID_PRIORITIES)}")
            while True:
                due_date = input("Enter due date (YYYY-MM-DD) or leave blank: ")
                if not due_date or Task.is_valid_date(due_date):
                    break
                print("Invalid date format. Please enter a valid date in the format YYYY-MM-DD.")
            todo_list.add_task(name, priority=priority, due_date=due_date)
            print("Task added successfully.")

        elif choice == "2":
            print("\nTasks:")
            display_tasks(todo_list.list_tasks())

        elif choice == "3":
            name = input("Enter the name of the task to mark as completed: ")
            if todo_list.mark_task_completed(name):
                print("Task marked as completed.")
            else:
                print("Task not found.")

        elif choice == "4":
            name = input("Enter the name of the task to edit: ")
            new_name = input("Enter new task name (or press Enter to skip): ")
            while True:
                new_priority = input("Enter new priority (Low, Normal, High) or press Enter to skip: ")
                if not new_priority or new_priority in Task.VALID_PRIORITIES:
                    break
                print(f"Invalid priority '{new_priority}'. Please enter one of: {', '.join(Task.VALID_PRIORITIES)}")
            while True:
                new_due_date = input("Enter new due date (YYYY-MM-DD) or press Enter to skip: ")
                if not new_due_date or Task.is_valid_date(new_due_date):
                    break
                print("Invalid date format. Please enter a valid date in the format YYYY-MM-DD.")
            if todo_list.edit_task(name, new_name=new_name, new_priority=new_priority, new_due_date=new_due_date):
                print("Task edited successfully.")
            else:
                print("Task not found.")

        elif choice == "5":
            status = input("Enter status to filter by (Pending or Completed): ")
            filtered_tasks = todo_list.filter_tasks_by_status(status)
            print(f"\nTasks with status '{status}':")
            display_tasks(filtered_tasks)

        elif choice == "6":
            confirm = input("Are you sure you want to clear all tasks? (yes/no): ").strip().lower()
            if confirm == "yes":
                todo_list.clear_tasks()
                print("All tasks cleared.")

        elif choice == "7":
            print("Exiting To-Do List Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
