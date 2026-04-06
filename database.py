import sqlite3

conn = sqlite3.connect("tasks.db", check_same_thread=False)
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT,
    deadline TEXT
)
""")

conn.commit()

def add_task(task, deadline):
    cursor.execute("INSERT INTO tasks (task, deadline) VALUES (?, ?)", (task, deadline))
    conn.commit()
    return "Task added successfully"

def get_tasks():
    cursor.execute("SELECT * FROM tasks")
    return cursor.fetchall()