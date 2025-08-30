# TODO list
print("Hi, Welcome to you To-Do List")
print("\n Hope you have a Productive day! \n")
tasks={}
task_num=1
status={}
while True:
    try:
        print("\n \n ---------To-Do List---------")
        print("1. Show tasks")
        print("2. Add a task")
        print("3. Mark a task as done")
        print("4. Exit the List")
        n = int(input("\n Enter your choice: "))

        if n == 1:
            print("\nTasks:")
            if len(tasks)==0:
                print("No tasks to display.")
            else:
                for key, value in tasks.items():
                    print(f'{key}. {value} - {status[value]}')
        elif n == 2:
            try:
                num = int(input("\n Number of tasks to be added: "))
                if num > 0:
                    for i in range(num):
                        task = str(input("\n Enter the task: "))
                        tasks[task_num] = task
                        status[task] = "Not Done"
                        task_num += 1
                        print("Task added!")
                else:
                    print("Please enter a positive number.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif n == 3:
            try:
                toBeDone = int(input("\n Enter task number to be marked as done: "))
                if toBeDone in tasks:
                    status[tasks[toBeDone]] = "Done"
                    print("Task marked as done!")
                else:
                    print(f"Error: Task number {toBeDone} does not exist.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif n == 4:
            break
        else:
            print("\nInvalid Input, Try again")
    except ValueError:
        print("\nInvalid input. Please enter a number from the menu.")

print("\n \n Thank you for using To-Do List")