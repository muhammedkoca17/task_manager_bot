import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from database import Database

class TestShowTasks(unittest.TestCase):
    def setUp(self):
        self.db = Database(":memory:")
    
    def test_show_tasks(self):
        self.db.add_task("Test1")
        self.db.add_task("Test2")
        tasks = self.db.get_all_tasks()
        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[0][1], "Test1")
        self.assertEqual(tasks[1][1], "Test2")

    def tearDown(self):
        self.db.close()

if __name__ == "__main__":
    unittest.main()