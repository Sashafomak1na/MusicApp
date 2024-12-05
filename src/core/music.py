import sqlite3

# Устанавливаем соединение с базой данных (или создаем ее)
conn = sqlite3.connect('music_app.db')

# Создаем курсор
cursor = conn.cursor()

# Создаем таблицу для пользователей
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
)
''')

# Создаем таблицу для музыкальных треков
cursor.execute('''
CREATE TABLE IF NOT EXISTS tracks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    artist TEXT NOT NULL,
    album TEXT,
    duration INTEGER  -- продолжительность в секундах
)
''')

# Создаем таблицу для избранных треков
cursor.execute('''
CREATE TABLE IF NOT EXISTS favorites (
    user_id INTEGER,
    track_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (track_id) REFERENCES tracks(id),
    PRIMARY KEY (user_id, track_id)
)
''')

# Сохраняем изменения и закрываем соединение
conn.commit()
conn.close()