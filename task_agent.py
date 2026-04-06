import sqlite3

conn = sqlite3.connect("tasks.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT,
    deadline TEXT
)
""")

conn.commit()

def handle_task(query):
    query = query.lower()

    if "add task" in query:
        cursor.execute("INSERT INTO tasks (task, deadline) VALUES (?, ?)", (query, "tomorrow"))
        conn.commit()
        return "Task added successfully"

    elif "show tasks" in query:
        cursor.execute("SELECT * FROM tasks")
        tasks = cursor.fetchall()

        return [
            {"id": t[0], "task": t[1], "deadline": t[2]}
            for t in tasks
        ]

    else:
        return "Task agent did not understand"