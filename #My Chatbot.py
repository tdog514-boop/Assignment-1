#My Chatbot
todo_list = []

def add_task():
    task = input("What task would you like to add? ")
    todo_list.append(task)
    print("Task added: ")

tasks = []

def handle_request():
    choice = input("Would you like to 'add', 'view', or 'complete' a task? ")

    if choice == "add":
        task = input("What task do you want to add? ")
        tasks.append(task)
        print("Task added!")

    elif choice == "view":
        if len(tasks) == 0:
            print("Your to-do list is empty.")
        else:
            print("Here are your tasks:")
            for i, task in enumerate(tasks, start=1):
                print(i, "-", task)

    elif choice == "complete":
        if len(tasks) == 0:
            print("No tasks to complete!")
        else:
            for i, task in enumerate(tasks, start=1):
                print(i, "-", task)
            done = int(input("Enter the number of the task you finished: "))
            if 1 <= done <= len(tasks):
                finished = tasks.pop(done - 1)
                print(f"Task '{finished}' marked as done!")
            else:
                print("That number doesn't match a task.")

    else:
        print("Please choose add, view, or complete.")

print("Welcome to your To-Do List Chatbot!")

handle_request()

while True:
    again = input("Do you want to do anything else? (y/n) ")
    if again == "y":
        handle_request()
    else:
        print("Goodbye! Have a great day!")
        break