from datetime import datetime


class Task:
    VALID_PRIORITIES = ["Low", "Normal", "High"]

    def __init__(self, name, status="Pending", priority="Normal", due_date=None):
        if priority not in self.VALID_PRIORITIES:
            raise ValueError(f"Invalid priority '{priority}'. Valid priorities are: {', '.join(self.VALID_PRIORITIES)}")
        if due_date and not self.is_valid_date(due_date):
            raise ValueError(f"Invalid due date '{due_date}'. Format must be YYYY-MM-DD.")
        self.name = name
        self.status = status
        self.priority = priority
        self.due_date = due_date

    @staticmethod
    def is_valid_date(date_str):
        """Validates that a string is in the format YYYY-MM-DD."""
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return True
        except ValueError:
            return False

    def __str__(self):
        return f"{self.name} (Status: {self.status}, Priority: {self.priority}, Due: {self.due_date or 'N/A'})"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, name, priority="Normal", due_date=None):
        """Adds a new task to the to-do list."""
        task = Task(name, priority=priority, due_date=due_date)
        self.tasks.append(task)

    def list_tasks(self):
        """Lists all tasks in the to-do list."""
        return self.tasks

    def mark_task_completed(self, task_name):
        """Marks a task as completed."""
        for task in self.tasks:
            if task.name == task_name:
                task.status = "Completed"
                return True
        return False

    def clear_tasks(self):
        """Clears the entire to-do list."""
        self.tasks.clear()

    def edit_task(self, task_name, new_name=None, new_priority=None, new_due_date=None):
        """Edits the details of an existing task."""
        for task in self.tasks:
            if task.name == task_name:
                if new_name:
                    task.name = new_name
                if new_priority:
                    if new_priority not in Task.VALID_PRIORITIES:
                        raise ValueError(
                            f"Invalid priority '{new_priority}'. Valid priorities are: {', '.join(Task.VALID_PRIORITIES)}"
                        )
                    task.priority = new_priority
                if new_due_date:
                    if not Task.is_valid_date(new_due_date):
                        raise ValueError("Invalid due date. Format must be YYYY-MM-DD.")
                    task.due_date = new_due_date
                return True
        return False

    def filter_tasks_by_status(self, status):
        """Filters tasks by their status."""
        return [task for task in self.tasks if task.status == status]
