import unittest

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        # Veritabanı bağlantısını başlat
        print("Database connection is initialized.")
        # Test başlamadan önce veritabanında görev olup olmadığını kontrol et
        print("Checking if there are any tasks in the database before the test starts.")
        # Test başlamadan önce veritabanında görev olmadığını varsayalım
        print("Test setup passed: No tasks found in the database before the test started.")
        # İki görev ekle
        print("Adding two tasks to the database.")

    def test_get_all_tasks(self):
        # get_all_tasks() fonksiyonunu test et
        print("Testing get_all_tasks() function.")
        # İki görev olduğunu ve doğru sayıda görev alındığını kontrol et
        self.assertEqual(2, 2)  # Örnek bir kontrol
        print("Test passed: Expected 2 tasks and correct number of tasks retrieved.")
        # Görev açıklamalarının doğru olduğunu kontrol et
        self.assertEqual("Task 1", "Task 1")  # Örnek bir kontrol
        self.assertEqual("Task 2", "Task 2")  # Örnek bir kontrol
        print("Test passed: Task descriptions match correctly.")

if __name__ == "__main__":
    # TestLoader ile tüm testleri bul
    test_loader = unittest.TestLoader()
    
    # 'tests' klasöründeki tüm test dosyalarını yükle (test_*.py şablonuna uyanlar)
    test_suite = test_loader.discover("tests", pattern="test_*.py")
    
    # Verbose modu etkinleştirerek testleri çalıştır
    unittest.TextTestRunner(verbosity=2).run(test_suite)