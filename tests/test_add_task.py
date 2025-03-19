import unittest
from database import Database

class TestAddTask(unittest.TestCase):
    def setUp(self):
        self.db = Database(":memory:")
    
    def test_add_task(self):
        task_id = self.db.add_task("Test görevi")
        tasks = self.db.get_all_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0][1], "Test görevi")

    def tearDown(self):
        self.db.close()

if __name__ == "__main__":
    unittest.main()