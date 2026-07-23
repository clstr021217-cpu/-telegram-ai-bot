import sqlite3

conn = sqlite3.connect("bot.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    user_id INTEGER PRIMARY KEY,
    username TEXT,
    credit INTEGER DEFAULT 10
)
""")

conn.commit()

def add_user(user_id, username):
    cursor.execute(
        "INSERT OR IGNORE INTO users(user_id, username) VALUES(?, ?)",
        (user_id, username)
    )
    conn.commit()

def get_credit(user_id):
    cursor.execute(
        "SELECT credit FROM users WHERE user_id=?",
        (user_id,)
    )
    row = cursor.fetchone()
    return row[0] if row else 0
