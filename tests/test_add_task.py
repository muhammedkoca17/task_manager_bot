import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from database import Database

class TestAddTask(unittest.TestCase):
    def setUp(self):
        self.db = Database(":memory:")
    
    def test_add_task(self):
        task_id = self.db.add_task("Test")
        task = self.db.get_task(task_id)
        self.assertEqual(task[1], "Test")
        self.assertEqual(task[2], 0)

    def tearDown(self):
        self.db.close()

if __name__ == "__main__":
    unittest.main()

if __name__ == "__main__":
    unittest.main()