import os
import datetime

class TaskManager():
    def __init__(self):
        self.tasks = {}

    def add_task(self, task):
        if task in self.tasks:
            print("Task already exists.")
            return
        self.tasks[task] = datetime.datetime.now().strftime("%H:%M")

    def remove_task(self, task):
        self.tasks.pop(task)
    
    def list_tasks(self):
        if len(self.tasks) == 0:
            print("No tasks. You're all done!")
        for task in self.tasks:
            print(f"[{self.tasks[task]}]: {task}")

if __name__ == "__main__":
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    print("Welcome to the task terminal! Enter 'help' for a list of commands.")

    task_manager = TaskManager()
    while True:
        request = input("[sudo] root/home> $ ")

        if request == "exit":
            break
        if request == "help":
            print("\n\nadd [task] - add a task\nremove [task] - remove a task\nlist - list all tasks\nexit - exit the program\n")
            continue
        if request == "clear":
            if os.name == "nt":
                os.system("cls")
            else:
                os.system("clear")
            continue
        if request.startswith("add "):
            task = request[4:]
            task_manager.add_task(task)
            print(f"Task '{task}' added.")
            continue
        if request.startswith("remove "):
            task = request[7:]
            if task in task_manager.tasks:
                task_manager.remove_task(task)
                print(f"Task '{task}' removed.")
                continue
            else:
                print(f"Task '{task}' not found.")
                continue
        if request == "list":
            task_manager.list_tasks()
            continue
        if request == "help invalid":
            print("The following reasons a command may be invalid:\n\n- The command does not exit.\n- You didn't pass the nessessary arguments.\n- You don't have valid permissions.\n")
            continue
        print("Invalid command. Type 'help' for a list of commands. Type 'help invalid' for more information on an invalid command.")