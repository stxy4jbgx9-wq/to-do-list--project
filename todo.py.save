tasks = []

print('to do list:')
tasks_input = input("Enter your tasks (separate them with commas): ")
tasks = tasks_input.split(",")

print("\nYour to-do list:")

for i in range(len(tasks)):
    print(i+1, ")", tasks[i].strip())

while True:
    print("\n---- OPTIONS ----")
    print("1. View tasks")
    print("2. Edit task")
    print("3. Delete task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nYour tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}) {task.strip()}")

    elif choice == "2":
        edit = int(input("Enter the task number to edit: "))
        new_task = input("Enter the new task: ")
        tasks[edit-1] = new_task

        print("\nUpdated list:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}) {task.strip()}")

    elif choice == "3":
        delete = int(input("Enter the task number to delete: "))
        tasks.pop(delete-1)

        print("\nTask deleted. Updated list:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}) {task.strip()}")

    elif choice == "4":
        print("exit")
        break

    else:
        print("Invalid choice.")
