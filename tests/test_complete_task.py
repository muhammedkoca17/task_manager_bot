import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from database import Database

class TestCompleteTask(unittest.TestCase):
    def setUp(self):
        self.db = Database(":memory:")
        self.task_id = self.db.add_task("Test")
    
    def test_complete_task(self):
        self.db.complete_task(self.task_id)
        self.assertEqual(self.db.get_task(self.task_id)[2], 1)

    def tearDown(self):
        self.db.close()

if __name__ == "__main__":
    unittest.main()