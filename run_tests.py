import unittest
import os
import sys
from database import Database
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        """Test öncesi hazırlıklar"""
        self.db = Database(":memory:")
        print("Database connection is initialized.")
        
        print("Checking if there are any tasks in the database before the test starts.")
        tasks = self.db.get_all_tasks()
        if len(tasks) == 0:
            print("Test setup passed: No tasks found in the database before the test started.")
        else:
            print("Test setup failed: Tasks found in the database before the test started.")
        
        self.db.add_task("Task 1")
        self.db.add_task("Task 2")
        print("Adding two tasks to the database.")

    def test_get_all_tasks(self):
        """get_all_tasks() fonksiyon testi"""
        print("\nTesting get_all_tasks() function.")
        
        tasks = self.db.get_all_tasks()
        
        # Görev sayısı kontrolü
        self.assertEqual(len(tasks), 2)
        print("Test passed: Expected 2 tasks and correct number of tasks retrieved.")
        
        # Görev içerik kontrolü
        self.assertEqual(tasks[0][1], "Task 1")
        self.assertEqual(tasks[1][1], "Task 2")
        print("Test passed: Task descriptions match correctly.")


    def tearDown(self):
        """Test sonrası temizlik"""
        self.db.close()

if __name__ == "__main__":
    unittest.main()
   