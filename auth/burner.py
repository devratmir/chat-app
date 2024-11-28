import sqlite3

conn = sqlite3.connect("auth/users.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE users")

cursor.execute("""
CREATE TABLE USERS (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username VARCHAR(49), 
        password VARCHAR(200),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
""")

conn.commit()