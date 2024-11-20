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
