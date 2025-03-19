import sqlite3
import unittest

class TaskManager:
    def __init__(self, db_path='tasks.db'):
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                description TEXT NOT NULL,
                completed BOOLEAN NOT NULL DEFAULT 0
            )
        ''')
        self.conn.commit()

    def add_task(self, description):
        cursor = self.conn.cursor()
        cursor.execute('INSERT INTO tasks (description) VALUES (?)', (description,))
        self.conn.commit()

    def get_all_tasks(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM tasks')
        return cursor.fetchall()

    def delete_task(self, task_id):
        cursor = self.conn.cursor()
        cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
        self.conn.commit()

    def complete_task(self, task_id):
        cursor = self.conn.cursor()
        cursor.execute('UPDATE tasks SET completed = 1 WHERE id = ?', (task_id,))
        self.conn.commit()

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.task_manager = TaskManager(':memory:')
        self.task_manager.add_task('Test task 1')
        self.task_manager.add_task('Test task 2')

    def test_get_all_tasks(self):
        tasks = self.task_manager.get_all_tasks()
        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[0][1], 'Test task 1')
        self.assertEqual(tasks[1][1], 'Test task 2')

    def test_delete_task(self):
        self.task_manager.delete_task(1)
        tasks = self.task_manager.get_all_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0][1], 'Test task 2')

    def test_complete_task(self):
        self.task_manager.complete_task(1)
        tasks = self.task_manager.get_all_tasks()
        self.assertEqual(tasks[0][2], 1)

    def tearDown(self):
        self.task_manager.conn.close()

if __name__ == '__main__':
    unittest.main()