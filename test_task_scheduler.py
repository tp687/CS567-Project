import unittest
import coverage
from datetime import datetime
from task_scheduler import Task, TaskManager


cov = coverage.Coverage()
cov.start()

class TestTask(unittest.TestCase):
    def test_task_creation(self):
        task = Task("1", "Test Task", "This is a test task")
        self.assertEqual(task.id, "1")
        self.assertEqual(task.name, "Test Task")
        self.assertEqual(task.description, "This is a test task")
        self.assertIsNone(task.due_date)
        self.assertFalse(task.is_completed)

    def test_set_due_date(self):
        task = Task("1", "Test Task", "This is a test task")
        task.set_due_date("2024-05-10")
        self.assertEqual(task.due_date, datetime(2024, 5, 10))

    def test_mark_completed(self):
        task = Task("1", "Test Task", "This is a test task")
        task.mark_completed()
        self.assertTrue(task.is_completed)

    def test_mark_incomplete(self):
        task = Task("1", "Test Task", "This is a test task")
        task.mark_completed()
        task.mark_incomplete()
        self.assertFalse(task.is_completed)

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.task_manager = TaskManager()
        self.task_manager.add_task(Task("1", "Test Task 1", "This is a test task 1"))
        self.task_manager.add_task(Task("2", "Test Task 2", "This is a test task 2", "2024-05-15"))

    def test_add_task(self):
        task_count_before = len(self.task_manager.tasks)
        self.task_manager.add_task(Task("3", "Test Task 3", "This is a test task 3"))
        task_count_after = len(self.task_manager.tasks)
        self.assertEqual(task_count_after, task_count_before + 1)

    def test_remove_task(self):
        task_count_before = len(self.task_manager.tasks)
        self.task_manager.remove_task("1")
        task_count_after = len(self.task_manager.tasks)
        self.assertEqual(task_count_after, task_count_before - 1)

    def test_edit_task(self):
        task = self.task_manager.tasks["1"]
        self.assertEqual(task.name, "Test Task 1")
        self.task_manager.edit_task("1", name="Updated Task")
        self.assertEqual(task.name, "Updated Task")

    def test_list_tasks(self):
        tasks = self.task_manager.list_tasks()
        self.assertTrue(tasks)

    def test_search_task(self):
        found_tasks = self.task_manager.search_task("Test Task 2")
        self.assertTrue(found_tasks)

    def test_mark_incomplete(self):
        task = self.task_manager.tasks["2"]
        task.mark_completed()
        self.assertTrue(task.is_completed)
        self.task_manager.mark_incomplete("2")
        self.assertFalse(task.is_completed)

    def test_sort_tasks_by_due_date(self):
        self.task_manager.add_task(Task("3", "Test Task 3", "This is a test task 3", "2024-05-05"))
        self.task_manager.sort_tasks("due_date")
        tasks = list(self.task_manager.tasks.values())
        self.assertEqual(tasks[0].name, "Test Task 3")
        self.assertEqual(tasks[1].name, "Test Task 2")

    def test_sort_tasks_by_completion_status(self):
        self.task_manager.tasks["1"].mark_completed()
        self.task_manager.sort_tasks("completion_status")
        tasks = list(self.task_manager.tasks.values())
        self.assertEqual(tasks[0].name, "Test Task 2")
        self.assertTrue(tasks[1].is_completed)

if __name__ == '__main__':
    unittest.main()

cov.stop()
cov.save()
cov.report()
