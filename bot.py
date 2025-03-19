import discord
import os
import sys
from discord.ext import commands
from dotenv import load_dotenv
from database import Database

# .env dosyasını yükle
load_dotenv()

# Botu başlat
tmb = commands.Bot(command_prefix="!", intents=discord.Intents.all())
db = Database()

# Bot sahibinin ID'sini al
OWNER_ID = int(os.getenv("OWNER_ID"))

@tmb.event
async def on_ready():
    print(f"{tmb.user.name} bağlandı!")

# Hata yönetimi
@tmb.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Geçersiz komut!")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Eksik parametre! Lütfen komutu doğru şekilde kullanın.")
    else:
        await ctx.send(f"Bir hata oluştu: {error}")

# Botu durdurma işlemi için özel bir fonksiyon
def shutdown_bot():
    print(f"{tmb.user.name} bağlantısı kesildi. Bot kapatılıyor...")
    sys.exit(0)

# Görev ekleme komutu
@tmb.command()
async def add_task(ctx, *, description):
    task_id = db.add_task(description)
    await ctx.send(f"Görev eklendi: {description}\nTüm görevleri görüntülemek için `!show_tasks` kullanın.")

# Görev silme komutu
@tmb.command()
async def delete_task(ctx, task_id: int):
    task = db.get_task(task_id)  # Veritabanından ID'ye göre görev al
    if not task:  # Eğer böyle bir görev yoksa
        await ctx.send("Bu ID'ye sahip bir görev bulunamadı!")
        return
    
    db.delete_task(task_id)  # Gerçek ID ile silme işlemi yapılır
    await ctx.send(f"ID: {task_id} olan görev silindi.")

# Görevleri listeleme komutu
@tmb.command()
async def show_tasks(ctx):
    tasks = db.get_all_tasks()
    if not tasks:
        await ctx.send("Hiç göreviniz yok.")
        return

    task_list = []
    for index, task in enumerate(tasks, start=1):  # Görevleri sıralı şekilde listele
        status = "✅" if task[2] else "❌"  # Tamamlanma durumunu belirle
        task_list.append(f"{index}. ID: {task[0]} - {task[1]} (Tamamlandı: {status})")  # Görev numarasını başta ekle
    
    await ctx.send("Görev Listesi:\n" + "\n".join(task_list))

# Görevi tamamlandı olarak işaretleme komutu
@tmb.command()
async def complete_task(ctx, task_id: int):
    task = db.get_task(task_id)  # Veritabanından ID'ye göre görev al
    if not task:  # Eğer böyle bir görev yoksa
        await ctx.send("Bu ID'ye sahip bir görev bulunamadı!")
        return

    db.complete_task(task_id)  # Gerçek ID ile işlemi yap
    await ctx.send(f"ID: {task_id} olan görev tamamlandı olarak işaretlendi.")

# Veritabanını sıfırlama komutu (sadece bot sahibi kullanabilir)
@tmb.command()
async def reset_db(ctx):
    if ctx.author.id == OWNER_ID:  # Sadece bot sahibi bu komutu kullanabilir
        db.reset_database()  # Veritabanını sıfırla
        await ctx.send("Veritabanı sıfırlandı. Tüm görevler silindi.")
    else:
        await ctx.send("Bu komutu kullanmaya yetkiniz yok!")

# Botu kapatma komutu (sadece bot sahibi kullanabilir)
@tmb.command()
async def shutdown(ctx):
    if ctx.author.id == OWNER_ID:  # Sadece bot sahibi bu komutu kullanabilir
        await ctx.send("Bot kapatılıyor...")
        print(f"{tmb.user.name} kapatılıyor...")  # Terminale yaz
        await tmb.close()
    else:
        await ctx.send("Bu komutu kullanma izniniz yok!")

# Botu çalıştır
try:
    token = os.getenv("DISCORD_BOT_TOKEN")
    tmb.run(token)
except KeyboardInterrupt:
    shutdown_bot()