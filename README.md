
# Discord Görev Yöneticisi Botu

Bu proje, Discord sunucularında küçük ekiplerin görevlerini yönetmek için tasarlanmış bir bottur. Görev ekleme, silme, görüntüleme ve tamamlama işlemlerini destekler. Tüm veriler SQLite veritabanında saklanır.

## discord.py
- **discord.py**, Discord için Python ile yazılmış, modern, kullanımı kolay, özellik açısından zengin ve asenkron bir API sarmalayıcısıdır. Bu kütüphane, Discord botları geliştirmek için güçlü ve esnek bir araç sunar.
- 
 ### Temel Özellikleri
 
 - **Modern ve Pythonic API:** async ve await kullanarak asenkron programlama desteği sağlar.

- **Oran Sınırlamaları:** Discord API'sinin oran sınırlamalarına uygun şekilde optimize edilmiştir.

- **Performans:** Hem hız hem de hafıza kullanımı açısından optimize edilmiştir.

- **Zengin Özellik Seti:** Mesaj yönetimi, ses desteği, kullanıcı ve sunucu yönetimi gibi birçok özellik sunar.

### Neden discord.py?
- **Kolay Kullanım**: Basit ve anlaşılır bir API yapısı sayesinde hızlıca bot geliştirebilirsiniz.

- **Geniş Topluluk Desteği:** Büyük bir geliştirici topluluğu ve zengin dokümantasyon desteği bulunmaktadır.

 - **Esneklik:** Hem küçük ölçekli botlar hem de büyük ölçekli projeler için uygundur.

### Daha Fazla Bilgi

- [discord.py Dokümantasyonu](https://discordpy.readthedocs.io/en/stable/)

- [Discord Developer Portal](https://discord.com/developers/docs/intro)
---

## 📋 Proje Özellikler
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
- pip install -r requirements.txt

## Bot Token'ını Ayarlayın:
- Proje dizininde .env dosyası oluşturun ve aşağıdaki bilgileri ekleyin:
- DISCORD_TOKEN alanına Discord bot token'ınızı, OWNER_ID alanına ise Discord kullanıcı ID'nizi girin.

## Botu Başlatın:
- python bot.py yada py bot.py deneyebilirsiniz.

## NOTLAR:
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
  
**Örnek Test Çıktısı:**
- ![image](https://github.com/user-attachments/assets/6f650065-5a12-4b26-85f6-083efc173c75)
- ![image](https://github.com/user-attachments/assets/373219af-274d-4b81-996a-7605e99d5810)


---

## 📂 Proje Yapısı
task_manager_bot/

├── bot.py

├── database.py

├── .gitignore

├── LICENCE

├── SECURITY.md


├── tests/

│ ├── test_add_task.py

│ ├── test_delete_task.py

│ └── ...
├── requirements.txt

├── README.md

└── tasks.db

---

## 👥 Katkıda Bulunanlar

- [Muhammed](https://github.com/dashboard)

---

## 📜 Lisans

Bu proje [MIT Lisansı](LICENSE) altında lisanslanmıştır.

---

### 🚀 Yapılan Geliştirmeler
## Veritabanı İyileştirmeleri:
- Görevler hem ID hem de görev numarası ile gösteriliyor, ancak işlemler (silme, tamamlama gibi) ID üzerinden yapılıyor.
  
![image](https://github.com/user-attachments/assets/fe2527e1-954b-44fd-a427-70d465cd7f01)


- Veritabanı sıfırlama işlevi eklendi: !reset_db komutu ile adminler veritabanını sıfırlayabiliyor.

- Hata yönetimi geliştirildi: Kullanıcı dostu hata mesajları ve loglama sistemi eklendi.
  
## Admin Komutları:
- !shutdown komutu ile adminler botu kapatabiliyor.
  ![image](https://github.com/user-attachments/assets/e2234ea5-251d-48cd-bcc4-6122eafdc0c1)

- !reset_db komutu ile adminler veritabanını sıfırlayabiliyor.
  ![image](https://github.com/user-attachments/assets/b84c49be-9d87-464a-8589-9b6d9cff100d)


## Görev Yönetimi:
- Görev ekleme, silme, tamamlama ve listeleme işlevleri tamamlandı.
- SQLite veritabanı kullanılarak görevler kalıcı hale getirildi.
  
## Hata Yönetimi:
- Kullanıcıların yanlış komut girmesi veya geçersiz işlem yapması durumunda hata mesajları eklendi.
- Botun kararlılığı artırıldı.
  
![image](https://github.com/user-attachments/assets/0e395d54-5ab8-463e-9a85-908d6cdaba3b)

### 🚀 Gelecekte Yapılaması Düşünülen Geliştirmeler
Projemizin gelecekteki sürümlerinde aşağıdaki özelliklerin eklenmesi planlanmaktadır:

### 1. Veritabanı İyileştirmeleri
- **Görev Tarihleri ve Son Tarihleri**:
  - Görevlere başlangıç ve bitiş tarihleri eklenecek.
  - Örnek: `!add_task "Projeyi tamamla" --start 2023-10-15 --end 2023-10-30`
  - Veritabanına `start_date` ve `end_date` sütunları eklenecek.

- **Görev Kategorileri**:
  - Görevler kategorilere ayrılacak (örneğin: İş, Kişisel, Acil).
  - Örnek: `!add_task "Alışveriş yap" --category Kişisel`
 
### 2. Kullanıcı Dostu Özellikler
- **Görev İstatistikleri**:
  - Kullanıcıların tamamladığı görevlerin istatistikleri gösterilecek.
  - Örnek: `!stats` → "Toplam 10 görev, 7 tamamlandı, 3 bekliyor."

- **Görev Öncelikleri**:
  - Görevlere öncelik seviyeleri eklenecek (Düşük, Orta, Yüksek).
  - Örnek: `!add_task "Sunumu hazırla" --priority Yüksek`
  
### 3. Güvenlik ve Yetkilendirme
- **Komut Kullanım Logları**:
  - Her komutun kim tarafından ve ne zaman kullanıldığı bir log dosyasına kaydedilecek.
  - Örnek: `bot.log` dosyasına `2023-10-15 14:30: User123 used !add_task`.
 
### 4. Gelişmiş Bot Özellikleri
- **Çoklu Dil Desteği**:
  - Bot birden fazla dilde kullanılabilir hale getirilecek.
  - Örnek: `!set_language TR` → Bot Türkçe dilinde çalışacak.
- **API Entegrasyonu**:
  - Harici API'lerle entegrasyon eklenecek (örneğin, hava durumu, Google Takvim, Trello).
  - Örnek: `!weather Istanbul` → İstanbul'un hava durumunu gösterecek.
    
### 5. Dokümantasyon ve Kullanıcı Rehberi
- **Komut Yardım Sistemi**:
  - Her komut için bir yardım mesajı eklenecek.
  - Örnek: `!help add_task` → "Görev eklemek için kullanılır. Örnek: `!add_task 'Alışveriş yap'`"
    
### 6. Bonus: Yenilikçi Özellikler
- **Oyunlaştırma**:
  - Görev tamamlayan kullanıcılara puanlar veya rozetler verilecek.
  - Örnek: `!leaderboard` → En çok görev tamamlayan kullanıcılar gösterilecek.
---
