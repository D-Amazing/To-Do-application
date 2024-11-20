# To-Do-application 
Core Features:

Add Tasks: Users can input and save tasks.
View Tasks: Lists all tasks or notifies the user if the list is empty.
Delete Tasks: Allows users to remove a specific task by its number.
Quit: Exits the application gracefully.
User Interaction:

Uses input() for user choices.
Validates user inputs to ensure they are appropriate for the selected operation.
Error Handling:

Empty List: Alerts the user if they try to view or delete tasks when no tasks exist.
Invalid Task Number: Ensures users can’t delete a task that isn’t in the list.
Invalid Menu Choice: Handles invalid main menu inputs gracefully.
Code Organization:

Functions for each operation improve readability and reusability.
Inline comments and docstrings explain the purpose of each function.
Testing and Edge Cases:

Empty List: Tested for viewing and deleting tasks when the list is empty.
Invalid Inputs: Handles non-integer inputs or out-of-range task numbers.
Unexpected Errors: Catches and displays any unanticipated exceptions. 

