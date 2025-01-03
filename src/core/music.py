import sqlite3

    conn = sqlite3.connect('music_app.db')
    cursor = conn.cursor()

    cursor.execute('''
       CREATE TABLE IF NOT EXISTS users (
           id INTEGER PRIMARY KEY AUTOINCREMENT,
           username TEXT NOT NULL UNIQUE,
           password TEXT NOT NULL,
           email TEXT NOT NULL UNIQUE
       )
       ''')

    cursor.execute('''
       CREATE TABLE IF NOT EXISTS tracks (
           id INTEGER PRIMARY KEY AUTOINCREMENT,
           title TEXT NOT NULL,
           artist TEXT NOT NULL,
           album TEXT,
       )
       ''')

    cursor.execute('''
       CREATE TABLE IF NOT EXISTS favorites (
           user_id INTEGER,
           track_id INTEGER,
           FOREIGN KEY (user_id) REFERENCES users(id),
           FOREIGN KEY (track_id) REFERENCES tracks(id),
           PRIMARY KEY (user_id, track_id)
       )
       ''')

    conn.commit()
    conn.close()