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
DISCORD_TOKEN=token_buraya
OWNER_ID =your_discord_ID

## Botu Başlatın:
python bot.py
