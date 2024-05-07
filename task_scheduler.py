import datetime

class Task:
    def __init__(self, id, name, description, due_date=None):
        self.id = id
        self.name = name
        self.description = description
        self.due_date = due_date
        self.is_completed = False

    def set_due_date(self, due_date):
        try:
            self.due_date = datetime.datetime.strptime(due_date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

    def mark_completed(self):
        self.is_completed = True

    def mark_incomplete(self):
        self.is_completed = False

    def __str__(self):
        due_date = self.due_date.strftime("%Y-%m-%d") if self.due_date else "No due date"
        status = "Completed" if self.is_completed else "Pending"
        return f"{self.id}: {self.name} - {due_date} ({status})"

class TaskManager:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task):
        if task.id in self.tasks:
            print("Task with this ID already exists.")
        else:
            self.tasks[task.id] = task

    def remove_task(self, id):
        if id in self.tasks:
            del self.tasks[id]
        else:
            print("Task not found.")

    def edit_task(self, id, name=None, description=None, due_date=None):
        if id in self.tasks:
            task = self.tasks[id]
            task.name = name if name else task.name
            task.description = description if description else task.description
            if due_date:
                task.set_due_date(due_date)
        else:
            print("Task not found.")

    def list_tasks(self):
        for task in self.tasks.values():
            print(task)

    def search_task(self, keyword):
        found_tasks = []
        for task in self.tasks.values():
            if keyword.lower() in task.name.lower() or keyword.lower() in task.description.lower():
                found_tasks.append(task)
        if found_tasks:
            for task in found_tasks:
                print(task)
        else:
            print("No matching tasks found.")

    def mark_incomplete(self, id):
        if id in self.tasks:
            self.tasks[id].mark_incomplete()
        else:
            print("Task not found.")

    def sort_tasks(self, sort_by):
        if sort_by == 'due_date':
            sorted_tasks = sorted(self.tasks.values(), key=lambda x: x.due_date)
        elif sort_by == 'completion_status':
            sorted_tasks = sorted(self.tasks.values(), key=lambda x: x.is_completed)
        else:
            print("Invalid sorting option.")
            return
        for task in sorted_tasks:
            print(task)

def main():
    task_manager = TaskManager()
    task_manager.add_task(Task("1", "Buy groceries", "Buy milk, bread, eggs", "2024-12-01"))
    task_manager.add_task(Task("2", "Doctor Appointment", "Annual check-up", "2024-12-15"))

    while True:
        print("\nTask Scheduler Menu")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Edit Task")
        print("4. List All Tasks")
        print("5. Search Task")
        print("6. Mark Task as Incomplete")
        print("7. Sort Tasks")
        print("8. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            id = input("Enter task ID: ")
            name = input("Enter task name: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            new_task = Task(id, name, description, due_date)
            task_manager.add_task(new_task)
        elif choice == '2':
            id = input("Enter task ID to remove: ")
            task_manager.remove_task(id)
        elif choice == '3':
            id = input("Enter task ID to edit: ")
            name = input("Enter new task name (press enter to skip): ")
            description = input("Enter new task description (press enter to skip): ")
            due_date = input("Enter new due date (YYYY-MM-DD, press enter to skip): ")
            task_manager.edit_task(id, name, description, due_date)
        elif choice == '4':
            task_manager.list_tasks()
        elif choice == '5':
            keyword = input("Enter keyword to search: ")
            task_manager.search_task(keyword)
        elif choice == '6':
            id = input("Enter task ID to mark as incomplete: ")
            task_manager.mark_incomplete(id)
        elif choice == '7':
            sort_by = input("Sort by (due_date/completion_status): ")
            task_manager.sort_tasks(sort_by)
        elif choice == '8':
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == '__main__':
    main()
