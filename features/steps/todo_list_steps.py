from behave import given, when, then
from todo_list import ToDoList

@given("the to-do list is empty")
def step_given_empty_list(context):
    context.todo_list = ToDoList()

@when('the user adds a task "{task_name}"')
def step_when_add_task(context, task_name):
    context.todo_list.add_task(task_name)

@then('the to-do list should contain "{task_name}"')
def step_then_contains_task(context, task_name):
    tasks = [task.name for task in context.todo_list.list_tasks()]
    assert task_name in tasks

@given('the to-do list contains tasks:')
def step_given_tasks(context):
    context.todo_list = ToDoList()
    for row in context.table:
        context.todo_list.add_task(row['Task'])

@when("the user lists all tasks")
def step_when_list_tasks(context):
    context.listed_tasks = context.todo_list.list_tasks()

@then("the output should contain:")
def step_then_output_contains(context):
    output = "\n".join([f"- {task.name}" for task in context.listed_tasks])
    assert context.text.strip() in output

@when('the user marks task "{task_name}" as completed')
def step_when_mark_completed(context, task_name):
    context.todo_list.mark_task_completed(task_name)

@then('the to-do list should show task "{task_name}" as completed')
def step_then_task_completed(context, task_name):
    task = next((t for t in context.todo_list.list_tasks() if t.name == task_name), None)
    assert task and task.status == "Completed"

@when("the user clears the to-do list")
def step_when_clear_list(context):
    context.todo_list.clear_tasks()

@then("the to-do list should be empty")
def step_then_empty_list(context):
    assert len(context.todo_list.list_tasks()) == 0

@when('the user edits the task "{task_name}" to have:')
def step_when_edit_task(context, task_name):
    new_data = {row['Field']: row['Value'] for row in context.table}
    context.todo_list.edit_task(
        task_name,
        new_name=new_data.get("Name"),
        new_priority=new_data.get("Priority"),
        new_due_date=new_data.get("Due Date"),
    )

@then('the to-do list should show:')
def step_then_list_contains_edited_task(context):
    for row in context.table:
        task_name = row['Task']
        task = next((t for t in context.todo_list.list_tasks() if t.name == task_name), None)
        assert task is not None
        assert task.status == row['Status']
        assert task.priority == row['Priority']
        assert task.due_date == row['Due Date']

@when('the user filters tasks by status "{status}"')
def step_when_filter_tasks(context, status):
    context.filtered_tasks = context.todo_list.filter_tasks_by_status(status)

@then("the output should contain:")
def step_then_filtered_output_contains(context):
    output = "\n".join([f"- {task.name}" for task in context.filtered_tasks])
    assert context.text.strip() in output
