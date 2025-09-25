# To-do list application in python

task = []

print("**__Welcome to the To-Do List App!__**")

while True:
    print("\nOptions: view / add / remove / exit")
    choice = input("Enter your choice: ")

    if choice == "add":
        item = input("Enter a task to add: ")
        task.append(item)
        print(f'"{item}" has been added to your to-do list.')
    elif choice == "view":
        if not task:
            print("Your to-do list is empty.")
        else:
            print("Your to-do list:")
            for i, t in enumerate(task, start=1):
                print(f"{i}. {t}")
    elif choice == "remove":
        task_num = int(input("Enter the task number to remove: "))
        if 0 < task_num <= len(task):   
            removed_task = task.pop(task_num - 1)
            print(f'"{removed_task}" has been removed from your to-do list.')
        else:
            print("Invalid task number.")
    elif choice == "exit":
        print("Exiting the To-Do List App. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
        