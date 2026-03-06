# load existing data
# create new item, list item, mark items as complete
# save items


import json
file_name = "todo_list.json"


def load():
    try:
        with open(file_name, 'r') as file:
            return json.load(file)
    except as :
        return {"tasks": []}


def save():
    try:
        with open(file_name, 'w') as file:
            json.dump(tasks, file)
    except:
        print("Something went wrong")


def check():
    pass


def create(tasks):
    description = input("Enter description: ").strip()
    if description:
        tasks["tasks"].append({"discription" : description, "complete": False})
        save(tasks)
        print("Tasks added")
    else:
        return print("Empty description")



def mark_task():
    pass


def main():
    tasks = load()
    print(tasks)

    while True:
        print("To-Do List manager!")
        print("1. View tasks")
        print("2. Add task")
        print("3. Finish task")
        print("4. Quit")

        choice = input("Enter your choice :").strip()
        if choice == "1":
            check()
        elif choice == "2":
            create()
        elif choice == "3":
            mark_task()
        elif choice == "4":
            print("Goodbye")
        else:
            print("Invalid choice. Choose again!")


list_task_manager = main()
print(list_task_manager)
