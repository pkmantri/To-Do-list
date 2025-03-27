import os

# Load tasks from a file
def load_tasks(filename="tasks.txt"):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return [line.strip() for line in file.readlines()]
    return []

# Save tasks to a file
def save_tasks(tasks, filename="tasks.txt"):
    with open(filename, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Display the menu
def display_menu():
    print("\nTo-Do List App")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Mark Task as Done")
    print("5. Exit")

# Main function
def todo_list():
    tasks = load_tasks()
    
    while True:
        display_menu()
        choice = input("Choose an option: ")
        
        if choice == "1":
            task = input("Enter task: ")
            tasks.append(task)
            save_tasks(tasks)
            print("Task added!")
        
        elif choice == "2":
            task = input("Enter task to remove: ")
            if task in tasks:
                tasks.remove(task)
                save_tasks(tasks)
                print("Task removed!")
            else:
                print("Task not found!")
        
        elif choice == "3":
            if tasks:
                print("\nYour Tasks:")
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")
            else:
                print("No tasks available!")
        
        elif choice == "4":
            if tasks:
                print("\nYour Tasks:")
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")
                task_index = int(input("Enter task number to mark as done: ")) - 1
                if 0 <= task_index < len(tasks):
                    tasks[task_index] = tasks[task_index] + " [Done]"
                    save_tasks(tasks)
                    print("Task marked as done!")
                else:
                    print("Invalid task number!")
            else:
                print("No tasks available!")
        
        elif choice == "5":
            print("Exiting...")
            break
        
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    todo_list()
