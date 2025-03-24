import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from database import Database

class TestDeleteTask(unittest.TestCase):
    def setUp(self):
        self.db = Database(":memory:")
        self.task_id = self.db.add_task("Test")
    
    def test_delete_task(self):
        self.db.delete_task(self.task_id)
        self.assertIsNone(self.db.get_task(self.task_id))

    def tearDown(self):
        self.db.close()
if __name__ == "__main__":
    unittest.main()