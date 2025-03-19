import unittest
from database import Database

class TestCompleteTask(unittest.TestCase):
    def setUp(self):
        self.db = Database(":memory:")
        self.db.add_task("Test görevi")
    
    def test_complete_task(self):
        self.db.complete_task(1)
        tasks = self.db.get_all_tasks()
        self.assertEqual(tasks[0][2], 1)  # completed = 1 (True)

    def tearDown(self):
        self.db.close()

if __name__ == "__main__":
    unittest.main()