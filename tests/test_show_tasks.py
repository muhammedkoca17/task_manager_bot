import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from database import Database

class TestShowTasks(unittest.TestCase):
    def setUp(self):
        self.db = Database(":memory:")
    
    def test_show_empty_tasks(self):
        """Boş görev listesi testi"""
        tasks = self.db.get_all_tasks()
        self.assertEqual(len(tasks), 0)

    def test_show_single_task(self):
        """Tek görev listeleme testi"""
        self.db.add_task("Test görevi 1")
        tasks = self.db.get_all_tasks()
        
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0][1], "Test görevi 1")
        self.assertEqual(tasks[0][2], 0)  # Tamamlanma durumu

    def test_show_multiple_tasks(self):
        """Çoklu Görev listeleme testi"""
        self.db.add_task("Test görevi 1")
        self.db.add_task("Test görevi 2")
        self.db.complete_task(1)  # İlk görevi tamamla
        
        tasks = self.db.get_all_tasks()
        self.assertEqual(len(tasks), 2)
        
        # Görevlerin sıralaması ve durumları
        self.assertEqual(tasks[0][0], 1)  # ID
        self.assertEqual(tasks[0][1], "Test görevi 1")
        self.assertEqual(tasks[0][2], 1)  # Tamamlanmış
        
        self.assertEqual(tasks[1][0], 2)  # ID
        self.assertEqual(tasks[1][1], "Test görevi 2")
        self.assertEqual(tasks[1][2], 0)  # Tamamlanmamış

    def tearDown(self):
        self.db.close()

if __name__ == "__main__":
    unittest.main()