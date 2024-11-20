def display_menu(): 
    """Display the main menu""" 
    print("\nTo-Do list application") 
    print("1. Add a task")
    print("2. View task")
    print("3. Delete a task") 
    print("4.Quit") 
    
def add_task(tasks):
    task = input("Enter the task: ").strip() 
    if task: 
        tasks.append(task) 
        print(f"Task '{task}' added successfully") 
    else:
        print("Task cannot be empty.") 

def view_tasks(tasks): 
    """View all tasks in the to-do list"""  
    if not tasks:
        print("your to-do list is empty.") 
    else:
        print("\nYour to-do list:") 
        for i, task in enumerate(tasks, start =1):
            print(f"{i}, {task}") 


def delete_task(tasks): 
    """Delete a specific task from the to-do list""" 
    
    if not tasks:
        print("Your to-do list is empty. Nothing to delete.") 
        return 

    view_tasks(tasks) 
    try: 
        task_number = int(input("\nEnter the number of the task to delete: ")) 
        if 1 <= task_number <= len(tasks): 
            removed_task = tasks.pop(task_number -1) 
            print(f"Task '{removed_task}' deleted successfully.") 
        else: 
            print("Invalid task number.") 
    except ValueError: 
        print("Please enter a valid number") 

def main(): 
    """Main function to run the to-do list application""" 
    tasks = [] 
    while True:
        try:
            display_menu() 
            choice = input("Enter your choice (1-4): ").strip() 
            if choice == '1':
                add_task(tasks) 
            elif choice == '2':
                view_tasks(tasks) 
            elif choice == '3':
                delete_task(tasks) 
            elif choice == '4': 
                print("Goodbye!") 
                break 
            else: 
                print("Invalid choice. Please select a number between 1 and 4.") 
        except Exception as e:
            print(f"An unexpected error occurred: {e}") 
        finally: 
            print("\nReturning to the main menu....") 
            
if __name__ == "__main__": 
    main() 
            
            
""" Features in Detail:
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

""" 
