Feature: Manage a To-Do List

Scenario: Add a task to the to-do list
  Given the to-do list is empty
  When the user adds a task "Buy groceries"
  Then the to-do list should contain "Buy groceries"

Scenario: List all tasks in the to-do list
  Given the to-do list contains tasks:
    | Task         |
    | Buy groceries|
    | Pay bills    |
  When the user lists all tasks
  Then the output should contain:
    """
    Tasks:
    - Buy groceries
    - Pay bills
    """

Scenario: Mark a task as completed
  Given the to-do list contains tasks:
    | Task          | Status   |
    | Buy groceries | Pending  |
  When the user marks task "Buy groceries" as completed
  Then the to-do list should show task "Buy groceries" as completed

Scenario: Clear the entire to-do list
  Given the to-do list contains tasks:
    | Task         |
    | Buy groceries|
    | Pay bills    |
  When the user clears the to-do list
  Then the to-do list should be empty

  Scenario: Edit a task in the to-do list
  Given the to-do list contains tasks:
    | Task          | Status   | Priority | Due Date  |
    | Buy groceries | Pending  | Normal   | 2025-01-10 |
  When the user edits the task "Buy groceries" to have:
    | Name         | Priority | Due Date   |
    | Grocery run  | High     | 2025-01-11 |
  Then the to-do list should show:
    | Task         | Status   | Priority | Due Date   |
    | Grocery run  | Pending  | High     | 2025-01-11 |

    Scenario: Filter tasks by status
  Given the to-do list contains tasks:
    | Task          | Status     |
    | Buy groceries | Completed  |
    | Pay bills     | Pending    |
  When the user filters tasks by status "Completed"
  Then the output should contain:
    """
    Tasks:
    - Buy groceries
    """
