#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "done": False})
        print(f"Task '{task}' added successfully.")

    def view_tasks(self):
        print("\n------ To-Do List ------")
        for i, task in enumerate(self.tasks, start=1):
            status = "Done" if task["done"] else "Not Done"
            print(f"{i}. {task['task']} ({status})")
        print("------------------------")

    def mark_done(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["done"] = True
            print(f"Task '{self.tasks[task_index]['task']}' marked as done.")
        else:
            print("Invalid task index. Please try again.")

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            deleted_task = self.tasks.pop(task_index)
            print(f"Task '{deleted_task['task']}' deleted.")
        else:
            print("Invalid task index. Please try again.")

def main():
    to_do_list = ToDoList()

    while True:
        print("\n------ To-Do List Menu ------")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            task = input("Enter the task: ")
            to_do_list.add_task(task)
        elif choice == "2":
            to_do_list.view_tasks()
        elif choice == "3":
            to_do_list.view_tasks()
            task_index = int(input("Enter the index of the task to mark as done: "))
            to_do_list.mark_done(task_index - 1)
        elif choice == "4":
            to_do_list.view_tasks()
            task_index = int(input("Enter the index of the task to delete: "))
            to_do_list.delete_task(task_index - 1)
        elif choice == "5":
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


# In[ ]:




