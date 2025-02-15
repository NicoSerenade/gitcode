import sys

list = []

def menu():
    while True:
        print("\nView tasks (1) \nMark a tasks as completed (2) \nAdd a task (3) \nDelete a task (4) \nExit (5) \n")
        choice = input("Enter the number: ")
        if choice.isdigit():
            choice = int(choice)
            if choice in range(1,6):
                return choice
            else:
                print("Invalid choice")
        else:
            print("Invlid choice")
    
# Pages

def view_task():
    if list:
        for i, task in enumerate(list):
            if task["status"]:
                print(f"Index: {i + 1}, Task: {task["name"]} ☑")
            else:
                print(f"Index: {i + 1}, Task: {task["name"]} ☐")
    else:
        print("\nThere's no pending tasks")

def mark_task():
    if list:
        while True:
            index = input("Enter the number of the task about to check: ")
            if index.isdigit():
                index = int(index) - 1
                if 0 <= index < len(list):
                    list[index]["status"] = True
                    break
                else:
                    print("Invalid choice")
            else:
                print("Invalid choice")
    else:
        print("\nThere's no pending tasks")
    
def add_task():
    name = input("Enter a new task: ")
    new_task = {"name": name, "status": False}
    list.append(new_task)
    
def delete_task():
    if list:
        while True:
            index = input("Enter the number of the task about to delete: ")
            if index.isdigit():
                index = int(index) - 1
                if 0 <= index < len(list):
                    del list[index]
                    break
                else:
                    print("Invalid choice")
            else:
                ("Invalid choice")
    else:
        print("\nThere's no pending tasks")
        
def show_page(chosen_page):
    if chosen_page == 1:
        view_task()
    elif chosen_page == 2:
        mark_task()
    elif chosen_page == 3:
        add_task()
    elif chosen_page ==4:
        delete_task()
    else:
        sys.exit("Great job, see ya!")
    
def main():
    while True:
        chosen_page = menu()
        show_page(chosen_page)

main()