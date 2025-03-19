import unittest

if __name__ == "__main__":
    # TestLoader ile tüm testleri bul
    test_loader = unittest.TestLoader()
    
    # 'tests' klasöründeki tüm test dosyalarını yükle (test_*.py şablonuna uyanlar)
    test_suite = test_loader.discover("tests", pattern="test_*.py")
    
    # Verbose modu etkinleştirerek testleri çalıştır
    unittest.TextTestRunner(verbosity=2).run(test_suite)