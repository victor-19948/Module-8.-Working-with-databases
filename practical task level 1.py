import sqlite3

with sqlite3.connect('db_17-51_07-08-2023.sqlite') as conn:
    conn.execute("PRAGMA foreign_keys = on")
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS Students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(32),
        surname VARCHAR(32),
        age INTEGER,
        city VARCHAR(32)
        )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Courses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        course VARCHAR(32),
        time_start DATETIME,
        time_end DATETIME
        )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Student_courses (
        student_id INTEGER,
        course_id INTEGER,
        FOREIGN KEY(student_id) REFERENCES Students(id)
        FOREIGN KEY(course_id) REFERENCES Courses(id)
        )''')
