from behave import given, when, then
from todo_list import ToDoList, Task


@given("the to-do list is empty")
def step_given_empty_todo_list(context):
    context.todo_list = ToDoList()


@when('the user adds a task "{task_name}"')
def step_when_add_task(context, task_name):
    context.todo_list.add_task(task_name)


@then('the to-do list should contain "{task_name}"')
def step_then_contains_task(context, task_name):
    tasks = [task.name for task in context.todo_list.list_tasks()]
    assert task_name in tasks, f"Task '{task_name}' not found in the to-do list."


@when("the user lists all tasks")
def step_when_list_tasks(context):
    context.listed_tasks = context.todo_list.list_tasks()
    context.output = "Tasks:\n" + "\n".join([f"- {task.name}" for task in context.listed_tasks])


@then("the output should contain:")
def step_then_output_contains(context):
    expected_output = context.text.strip()
    assert expected_output in context.output, f"Expected:\n{expected_output}\nBut got:\n{context.output}"


@when('the user marks task "{task_name}" as completed')
def step_when_mark_completed(context, task_name):
    context.todo_list.mark_task_completed(task_name)


@then('the to-do list should show task "{task_name}" as completed')
def step_then_task_completed(context, task_name):
    task = next((t for t in context.todo_list.list_tasks() if t.name == task_name), None)
    assert task and task.status == "Completed", f"Task '{task_name}' is not marked as completed."


@when("the user clears the to-do list")
def step_when_clear_list(context):
    context.todo_list.clear_tasks()


@then("the to-do list should be empty")
def step_then_empty_list(context):
    assert len(context.todo_list.list_tasks()) == 0, "The to-do list is not empty."


@when('the user edits the task "{task_name}" to have:')
def step_when_edit_task(context, task_name):
    new_data = {row["Field"]: row["Value"] for row in context.table}
    context.todo_list.edit_task(
        task_name,
        new_name=new_data.get("Name"),
        new_priority=new_data.get("Priority"),
        new_due_date=new_data.get("Due Date"),
    )


@then('the to-do list should show:')
def step_then_list_contains_edited_task(context):
    for row in context.table:
        task_name = row["Task"]
        task = next((t for t in context.todo_list.list_tasks() if t.name == task_name), None)
        assert task is not None, f"Task '{task_name}' not found."
        assert task.status == row["Status"], f"Expected status '{row['Status']}' but got '{task.status}'."
        assert task.priority == row["Priority"], f"Expected priority '{row['Priority']}' but got '{task.priority}'."
        assert task.due_date == row["Due Date"], f"Expected due date '{row['Due Date']}' but got '{task.due_date}'."


@when('the user filters tasks by status "{status}"')
def step_when_user_filters_tasks_by_status(context, status):
    context.filtered_tasks = context.todo_list.filter_tasks_by_status(status)
    context.output = "Tasks:\n" + "\n".join([f"- {task.name}" for task in context.filtered_tasks])


@given("the to-do list contains tasks")
def step_given_todo_list_contains_tasks(context):
    context.todo_list = ToDoList()
    for row in context.table:
        task_name = row["Task"]
        task_priority = row.get("Priority", "Normal")
        task_due_date = row.get("Due Date", None)
        task_status = row.get("Status", "Pending")
        context.todo_list.add_task(task_name, priority=task_priority, due_date=task_due_date)
        if task_status == "Completed":
            context.todo_list.mark_task_completed(task_name)


@then("the to-do list should show")
def step_then_todo_list_should_show(context):
    for row in context.table:
        task_name = row["Task"]
        task = next((t for t in context.todo_list.list_tasks() if t.name == task_name), None)
        assert task is not None, f"Task '{task_name}' not found."
        assert task.status == row["Status"], f"Expected status '{row['Status']}' but got '{task.status}'."
        assert task.priority == row["Priority"], f"Expected priority '{row['Priority']}' but got '{task.priority}'."
        assert task.due_date == row["Due Date"], f"Expected due date '{row['Due Date']}' but got '{task.due_date}'."

@then("the output should contain")
def step_then_output_should_contain(context):
    expected_output = "\n".join(line.strip() for line in context.text.strip().splitlines())
    actual_output = "\n".join(line.strip() for line in context.output.strip().splitlines())
    assert expected_output == actual_output, f"Expected:\n{expected_output}\nBut got:\n{actual_output}"


@when('the user edits the task "{task_name}" to have')
def step_when_user_edits_task(context, task_name):
    new_data = {}
    for row in context.table:
        if "Name" in row:
            new_data["new_name"] = row["Name"]
        if "Priority" in row:
            new_data["new_priority"] = row["Priority"]
        if "Due Date" in row:
            new_data["new_due_date"] = row["Due Date"]

    success = context.todo_list.edit_task(
        task_name,
        new_name=new_data.get("new_name"),
        new_priority=new_data.get("new_priority"),
        new_due_date=new_data.get("new_due_date"),
    )

    assert success, f"Task '{task_name}' not found or could not be updated."



