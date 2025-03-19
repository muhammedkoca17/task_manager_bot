# task_manager_bot
=======
# Discord Görev Yöneticisi Botu

Bu proje, Discord sunucularında küçük ekiplerin görevlerini yönetmek için tasarlanmış bir bottur. Görev ekleme, silme, görüntüleme ve tamamlama işlemlerini destekler. Tüm veriler SQLite veritabanında saklanır.

---

## 📋 Özellikler
- **Görev Ekleme**: `!add_task <açıklama>` ile yeni görev ekleyin.
- **Görev Silme**: `!delete_task <görev_numarası>` ile görev silin.
- **Görevleri Görüntüleme**: `!show_tasks` ile tüm görevleri listeleyin.
- **Görev Tamamlama**: `!complete_task <görev_numarası>` ile görevi tamamlandı olarak işaretleyin.
- **Veritabanı Sıfırlama**: `!reset_db` ile veritabanını sıfırlayın (sadece bot sahibi).
- **Botu Kapatma**: `!shutdown` ile botu kapatın (sadece bot sahibi).

---

## 🛠️ Kurulum

### Gereksinimler
- Python 3.10 veya üzeri
- Discord hesabı ve bot tokenı ([Nasıl Alınır?](https://discordpy.readthedocs.io/en/stable/discord.html))

### Adımlar
1. Depoyu klonlayın:
   ```bash
   git clone https://github.com/muhammedkoca17/task_manager_bot.git
   cd task_manager_bot

## Bağımlılıkları Yükleyin:
pip install -r requirements.txt

## Bot Token'ını Ayarlayın:
- DISCORD_TOKEN=token_buraya
- OWNER_ID =your_discord_ID

## Botu Başlatın:
- python bot.py

---

## 📝 Kullanım Örnekleri (RESİM)

### Görev Ekleme: `!add_task <açıklama>`
 ![task_added](https://github.com/user-attachments/assets/9d4ae87f-bd6d-4d77-97cc-bcfb9b4fd256)

### Görevleri Listeleme : `!show_tasks`
![task_show_1](https://github.com/user-attachments/assets/43510674-a9bd-41a4-9cba-8f010c1d70aa)
![task_show_2](https://github.com/user-attachments/assets/49cf2175-ab46-417d-9535-75df6a535430)

### Görev Tamamlama: `!complete_task <görev_numarası>`
![task_complete](https://github.com/user-attachments/assets/50e35fd6-934c-4c7c-ba2f-bbd5dafc7963)

### Görev Silme: `!delete_task <görev_numarası>`
![task_delete](https://github.com/user-attachments/assets/c1f48aa5-5464-4cc5-b9a1-d5af695f92b3)

---

## 🧪 Testler

Testleri çalıştırmak için:
- python run_tests.py
- ![tests_results](https://github.com/user-attachments/assets/9414e82f-e36d-48c6-b141-03cfa3685aa1)


**Örnek Test Çıktısı:** (RESİM)
✅ Veritabanı bağlantısı başlatıldı.
✅ Test başladı: Veritabanında önceden görev bulunmuyor.
✅ 2 görev başarıyla eklendi.
✅ Görev açıklamaları doğru eşleşiyor.
---

## 📂 Proje Yapısı
task_manager_bot/

├── bot.py

├── database.py

├── tests/

│ ├── test_add_task.py

│ ├── test_delete_task.py

│ └── ...
├── requirements.txt

├── README.md

└── .env

---

## 👥 Katkıda Bulunanlar

- [Muhammed](https://github.com/dashboard)

---

## 📜 Lisans

Bu proje [MIT Lisansı](LICENSE) altında lisanslanmıştır.

---

## 🚀 Gelecek Geliştirmeler
- Yetkilendirme sistemi
- Görev hatırlatıcıları
- Çoklu sunucu desteği
- Dil desteği

---
