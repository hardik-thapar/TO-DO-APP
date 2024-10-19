import calendar
from datetime import datetime
from colorama import init, Fore
# This is a simple to do list 
# appplication with a little bit different
# features, you can add , update and mark 
# your tasks complete and organise your daily tasks.
# Initialize Colorama
init(autoreset=True)

current_date = datetime.now()

def print_border():
    border_length = 60  # You can adjust this length
    print(Fore.YELLOW + '*' * border_length)

def task():
    tasks = []
    completed = []
    updated = []

    print_border()
    print(Fore.GREEN + '### Welcome to the Task Manager application ###')
    print(Fore.CYAN + "-- This application is created by Hardik Thapar --")
    print(Fore.BLUE + "📅  Current date:", current_date.strftime("%Y-%m-%d"), " 📅")
    print_border()
    
    while True:
        print()
        print(Fore.MAGENTA + 'Select from this menu:')
        print(Fore.BLUE + '''
1. 📝  Add a task
2. 📋  View all tasks
3. ✅  Mark task as done
4. 🔄  Update a task
5. 📜  View completed/updated history
6. ❌  Exit''')
        
        try:
            operator = int(input(Fore.WHITE + "\nEnter your choice : "))
            if operator == 1:
                new_task = input(Fore.WHITE + "Enter the task : ")
                tasks.append(new_task)
                print(Fore.GREEN + "Task added successfully! ✅")
            elif operator == 2:
                if tasks:
                    print(Fore.BLUE + "Current tasks:")
                    for idx, task in enumerate(tasks):
                        print(Fore.CYAN + f"{idx}. {task} 📌")
                else:
                    print(Fore.RED + "No tasks available. 🗒️")
            elif operator == 3:
                if tasks:
                    print(Fore.BLUE + "Current tasks:")
                    for idx, task in enumerate(tasks):
                        print(Fore.CYAN + f"{idx}. {task}")
                    try:
                        delete_task = int(input(Fore.WHITE + "Enter the task number you have completed : "))
                        if 0 <= delete_task < len(tasks):
                            confirm = input(Fore.WHITE + f"Are you sure you have completed the task '{tasks[delete_task]}'? (yes/no) : ")
                            if confirm.lower() == "yes":
                                completed.append(tasks[delete_task])
                                del tasks[delete_task]
                                print(Fore.GREEN + "Task marked as completed! ✅")
                            else:
                                print(Fore.YELLOW + "Task not marked as completed.")
                        else:
                            print(Fore.RED + "Invalid task number. ❌")
                    except ValueError:
                        print(Fore.RED + "Please enter a valid number. ❌")
                else:
                    print(Fore.RED + "No tasks available to mark as done. ❌")
            elif operator == 4:
                if tasks:
                    print(Fore.BLUE + "Current tasks:")
                    for idx, task in enumerate(tasks):
                        print(Fore.CYAN + f"{idx}. {task}")
                    try:
                        ind = int(input(Fore.WHITE + "Enter the task number you want to update : "))
                        if 0 <= ind < len(tasks):
                            updated.append(tasks[ind])
                            tasks[ind] = input(Fore.WHITE + "Enter the updated task : ")
                            print(Fore.GREEN + "Task updated successfully! 🔄")
                        else:
                            print(Fore.RED + "Invalid task number. ❌")
                    except ValueError:
                        print(Fore.RED + "Please enter a valid number. ❌")
                else:
                    print(Fore.RED + "No tasks available to update. ❌")
            elif operator == 5:
                print(Fore.BLUE + "📜 History:")
                if completed:
                    print(Fore.GREEN + "Completed tasks ✅", completed)
                else:
                    print(Fore.RED + "No completed tasks to display.")
                if updated:
                    print(Fore.CYAN + "Updated tasks 📝", updated)
                else:
                    print(Fore.RED + "No updated tasks to display.")
            elif operator == 6:
                print(Fore.YELLOW + "⚠️..CONFIRM..⚠️")
                confirm_exit = input(Fore.WHITE + "Are you sure you want to exit? (yes/no) : ")
                if confirm_exit.lower() == "yes":
                    print(Fore.RED + "❌ Exiting the app... Goodbye! ❌")
                    break
            else:
                print(Fore.RED + "Invalid choice. Please select a valid option. ❌")
        except ValueError:
            print(Fore.RED + "Please enter a valid number. ❌")

    print_border()

# Start the task manager
task()