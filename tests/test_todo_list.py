import pytest
from todo_list import ToDoList

def test_add_task():
    todo_list = ToDoList()
    todo_list.add_task("Buy groceries")
    assert len(todo_list.list_tasks()) == 1

def test_mark_task_completed():
    todo_list = ToDoList()
    todo_list.add_task("Buy groceries")
    assert todo_list.mark_task_completed("Buy groceries")
    assert todo_list.list_tasks()[0].status == "Completed"

def test_clear_tasks():
    todo_list = ToDoList()
    todo_list.add_task("Buy groceries")
    todo_list.clear_tasks()
    assert len(todo_list.list_tasks()) == 0
