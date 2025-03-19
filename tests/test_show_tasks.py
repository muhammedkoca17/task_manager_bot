import unittest
from database import Database

class TestShowTasks(unittest.TestCase):
    def setUp(self):
        self.db = Database(":memory:")
        self.db.add_task("Test görevi 1")
        self.db.add_task("Test görevi 2")
    
    def test_show_tasks(self):
        tasks = self.db.get_all_tasks()
        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[0][1], "Test görevi 1")
        self.assertEqual(tasks[1][1], "Test görevi 2")

    def tearDown(self):
        self.db.close()

if __name__ == "__main__":
    unittest.main()