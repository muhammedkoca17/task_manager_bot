import sqlite3

class Database:
    def __init__(self, db_path="tasks.db"):
        self.connection = sqlite3.connect(db_path)  # Veritabanı bağlantısını oluştur
        self.cursor = self.connection.cursor()  # Cursor oluştur
        self.create_table()

    def create_table(self):
        """Tasks tablosunu oluşturur (eğer yoksa)."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                description TEXT NOT NULL,
                completed BOOLEAN NOT NULL DEFAULT 0
            )
        """)
        self.connection.commit()
    
    def add_task(self, description):
        """Yeni görev ekler (boş görevleri engeller)"""
        if not description or not description.strip():
            raise ValueError("Görev açıklaması boş olamaz!")
    
        self.cursor.execute("INSERT INTO tasks (description, completed) VALUES (?, ?)", 
                       (description.strip(), 0))
        self.connection.commit()
        return self.cursor.lastrowid

    def delete_task(self, task_id):
        """Belirtilen ID'ye sahip görevi siler.."""
        self.cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        self.connection.commit()

    def complete_task(self, task_id):
        """Belirtilen görevi tamamlandı olarak işaretler."""
        self.cursor.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))
        self.connection.commit()

    def get_task(self, task_id):
        """Belirtilen ID'ye sahip görevi döndürür."""
        self.cursor.execute("SELECT id, description, completed FROM tasks WHERE id = ?", (task_id,))
        return self.cursor.fetchone()

    def get_all_tasks(self):
        """Tüm görevleri döndürür."""
        self.cursor.execute("SELECT id, description, completed FROM tasks")
        return self.cursor.fetchall()

    def reset_database(self):
        """Tüm görevleri siler ve veritabanını sıfırlar."""
        self.cursor.execute("DELETE FROM tasks")  # Tüm görevleri sil
        self.cursor.execute("UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME='tasks'")  # AUTOINCREMENT'i sıfırla
        self.connection.commit()
    
    def close(self):
        """Veritabanı bağlantısını kapatır."""
        self.connection.close()
