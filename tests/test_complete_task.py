import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from database import Database

class TestCompleteTask(unittest.TestCase):
    def setUp(self):
        self.db = Database(":memory:")
        self.task_id = self.db.add_task("Test görevi")
    
    def test_complete_existing_task(self):
        """Varr olan görevi tamamlama testi"""
        self.db.complete_task(self.task_id)
        task = self.db.get_task(self.task_id)
        self.assertEqual(task[2], 1)  # completed = 1 (True)

    def test_complete_nonexistent_task(self):
        """Var olmayan görevi tamamlama testi"""
        non_existent_id = 999
        self.db.complete_task(non_existent_id)  # Hata vermemeli
        # Veritabanında değişiklik olmamalı
        tasks = self.db.get_all_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0][2], 0)  # Tamamlanma durumu değişmemeli

    def test_complete_already_completed_task(self):
        """Zaten tamamlanmış görevi tekrar tamamlama testi"""
        # İlk tamamlama
        self.db.complete_task(self.task_id)
        # İkinci tamamlama
        self.db.complete_task(self.task_id)
        
        task = self.db.get_task(self.task_id)
        self.assertEqual(task[2], 1)  # Yine tamamlanmış olmalı

    def tearDown(self):
        self.db.close()

if __name__ == "__main__":
    unittest.main()