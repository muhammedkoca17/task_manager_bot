import unittest
from database import Database

class TestDeleteTask(unittest.TestCase):
    def setUp(self):
        self.db = Database(":memory:")
        self.db.add_task("Test görevi")
    
    def test_delete_task(self):
        self.db.delete_task(1)
        tasks = self.db.get_all_tasks()
        self.assertEqual(len(tasks), 0)

    def tearDown(self):
        self.db.close()

if __name__ == "__main__":
    unittest.main()