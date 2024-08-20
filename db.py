import sqlite3

connect = sqlite3.connect("database.db")
cursor = connect.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name VARCHAR(255),
    username VARCHAR(255),
    user_id INTEGER
     )
''')

connect.commit()


class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def add_user(self, full_name, username, user_id):
        with self.connection:
            return self.cursor.execute('INSERT INTO users (full_name, username, user_id) VALUES (?, ?, ?)',
                                       (full_name, username, user_id))

    def check_user(self, user_id):
        with self.connection:
            return self.cursor.execute("SELECT user_id FROM 'users' WHERE user_id = ?", (user_id,)).fetchone()


connect.close()
