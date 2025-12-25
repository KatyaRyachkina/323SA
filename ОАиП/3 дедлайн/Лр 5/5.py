class Task:
    def __init__(self, description, priority):
        self.description = description
        self.priority = priority

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, priority):
        new_task = Task(description, priority)
        self.tasks.append(new_task)

    def show_tasks(self):
        for task in self.tasks:
            print(f"{task.description} - {task.priority}")

manager = TaskManager()
manager.add_task("Помыть посуду", 2)
manager.add_task("Подготовить отчет", 8)
manager.show_tasks()
