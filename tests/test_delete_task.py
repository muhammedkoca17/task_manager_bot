import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from database import Database

class TestDeleteTask(unittest.TestCase):
    def setUp(self):
        self.db = Database(":memory:")
        self.db.add_task("Test görevi")
    
    def test_delete_task(self):
        print("delete_task fonksiyonu test ediliyor....")
        self.db.delete_task(1)
        tasks = self.db.get_all_tasks()
        self.assertEqual(len(tasks), 0)
        print("delete_task fonksiyonu başarılı.")

    def tearDown(self):
        self.db.close()

if __name__ == "__main__":
    unittest.main()