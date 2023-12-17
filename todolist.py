def display_tasks(task_list):
    if not task_list:
        print("No tasks available.")
    else:
        print("Tasks:")
        for task, status in task_list.items():
            print(f"{task}: {'Done' if status else 'Not Done'}")

def add_task(task_list):
    task = input("Enter the task: ")
    task_list[task] = False  # Status is initially set to 'Not Done'
    print(f"Task '{task}' added successfully.")

def mark_task_as_done(task_list):
    task = input("Enter the task to mark as done: ")
    if task in task_list:
        task_list[task] = True
        print(f"Task '{task}' marked as done.")
    else:
        print("Task not found.")

def main():
    tasks = {}

    while True:
        print("\nTo-Do List Menu:")
        print("1. Display Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_task_as_done(tasks)
        elif choice == "4":
            print("Quitting the To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
    