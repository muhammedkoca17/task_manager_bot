import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from database import Database

class TestAddTask(unittest.TestCase):
    def setUp(self):
        self.db = Database(":memory:")
    
    def test_add_single_task(self):
        """Tek bir görev ekleme testi"""
        task_id = self.db.add_task("Test görevi")
        self.assertIsInstance(task_id, int)
        
        tasks = self.db.get_all_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0][1], "Test görevi")
        self.assertEqual(tasks[0][2], 0)  # Başlangıçta tamamlanmamış olmalı

    def test_add_multiple_tasks(self):
        """Çoklu görev ekleme testi"""
        ids = [self.db.add_task(f"Görev {i}") for i in range(1, 4)]
        
        tasks = self.db.get_all_tasks()
        self.assertEqual(len(tasks), 3)
        for i, task in enumerate(tasks, start=1):
            self.assertEqual(task[1], f"Görev {i}")

    def test_add_empty_task(self):
        """Boş görev eklemenin engellendiğini test eder"""
        with self.assertRaises(ValueError):  # ValueError bekliyoruz
            self.db.add_task("")  # Boş string
        with self.assertRaises(ValueError):
            self.db.add_task("   ")  # Sadece boşluklar

    def tearDown(self):
        self.db.close()

if __name__ == "__main__":
    unittest.main()