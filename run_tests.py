import unittest
import sys
import os
from database import Database

# Testlerin bulunduğu dizini Python yoluna ekle
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'tests')))

class TestTaskManager(unittest.TestCase):
    """Veritabanı işlemlerini test eden ana sınıf"""
    
    def setUp(self):
        """Her test öncesi çalışacak kurulum"""
        self.db = Database(":memory:")
        self.initial_tasks = [
            ("Task 1", 0),
            ("Task 2", 1),  # Tamamlanmış görev
            ("Task 3", 0)
        ]
        
        # Başlangıç görevlerini ekle
        for desc, completed in self.initial_tasks:
            task_id = self.db.add_task(desc)
            if completed:
                self.db.complete_task(task_id)
        
        print("\nTest veritabanı başlangıç durumu:")
        for task in self.db.get_all_tasks():
            print(f"ID: {task[0]}, Desc: {task[1]}, Completed: {task[2]}")

    def test_get_all_tasks(self):
        """Tüm görevleri getirme fonksiyonunu test eder"""
        tasks = self.db.get_all_tasks()
        
        # Görev sayısı kontrolü
        self.assertEqual(len(tasks), len(self.initial_tasks))
        
        # Görev içerikleri kontrolü
        for i, task in enumerate(tasks):
            self.assertEqual(task[1], self.initial_tasks[i][0])  # Açıklama
            self.assertEqual(task[2], self.initial_tasks[i][1])  # Tamamlanma durumu

    def test_add_task(self):
        """Yeni görev ekleme fonksiyonunu test eder"""
        new_desc = "Yeni Test Görevi"
        new_id = self.db.add_task(new_desc)
        
        # Eklenen görevi kontrol et
        task = self.db.get_task(new_id)
        self.assertEqual(task[1], new_desc)
        self.assertEqual(task[2], 0)  # Yeni görev tamamlanmamış olmalı

    def test_complete_task(self):
        """Görev tamamlama fonksiyonunu test eder"""
        task_id = 1  # İlk görevin ID'si
        self.db.complete_task(task_id)
        
        # Tamamlanma durumunu kontrol et
        task = self.db.get_task(task_id)
        self.assertEqual(task[2], 1)

    def test_delete_task(self):
        """Görev silme fonksiyonunu test eder"""
        task_id = 2  # Silinecek görev ID'si
        initial_count = len(self.db.get_all_tasks())
        
        self.db.delete_task(task_id)
        
        # Görev sayısı azalmış mı kontrol et
        tasks = self.db.get_all_tasks()
        self.assertEqual(len(tasks), initial_count - 1)
        
        # Silinen görev artık getirilemiyor mu kontrol et
        self.assertIsNone(self.db.get_task(task_id))

    def tearDown(self):
        """Her test sonrası çalışacak temizlik"""
        self.db.close()
        print("Test tamamlandı, veritabanı bağlantısı kapatıldı.\n")

def run_all_tests():
    """Tüm testleri çalıştırır ve rapor oluşturur"""
    # Tüm test modüllerini bul
    test_loader = unittest.TestLoader()
    test_suite = unittest.TestSuite()
    
    # Ana test sınıfını ekle
    test_suite.addTests(test_loader.loadTestsFromTestCase(TestTaskManager))
    
    # 'tests' klasöründeki diğer testleri ekle
    test_modules = [
        'test_add_task',
        'test_complete_task',
        'test_delete_task',
        'test_show_tasks'
    ]
    
    for module in test_modules:
        try:
            mod = __import__(f'tests.{module}', fromlist=['*'])
            test_suite.addTests(test_loader.loadTestsFromModule(mod))
        except ImportError as e:
            print(f"Test modülü yüklenemedi: {module} - {str(e)}")
    
    # Testleri çalıştır
    test_runner = unittest.TextTestRunner(verbosity=2)
    result = test_runner.run(test_suite)
    
    # Sonuç raporu
    print("\n" + "="*50)
    print("TEST SONUÇLARI")
    print(f"Toplam Test: {result.testsRun}")
    print(f"Başarılı: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Başarısız: {len(result.failures)}")
    print(f"Hatalar: {len(result.errors)}")
    print("="*50)
    
    return result.wasSuccessful()

if __name__ == "__main__":
    # Sadece bu dosyadaki testleri çalıştırmak için:
    # unittest.main()
    
    # Tüm testleri çalıştırmak için:
    run_all_tests()