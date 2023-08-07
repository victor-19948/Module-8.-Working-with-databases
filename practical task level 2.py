import datetime
import sqlite3

with sqlite3.connect('db_17-51_07-08-2023.sqlite') as conn:
    cursor = conn.cursor()

    cursor.executemany('INSERT INTO Students (name, surname, age, city) VALUES (?, ?, ?, ?)',
                       [
                           ('Max', 'Brooks', 24, 'Spb'),
                           ('John', 'Stones', 15, 'Spb'),
                           ('Andy', 'Wings', 45, 'Manhester'),
                           ('Kate', 'Brooks', 34, 'Spb')
                       ]
                       )

    cursor.executemany('INSERT INTO Courses (course, time_start, time_end) VALUES (?, ?, ?)',
                       [
                           ('python', datetime.date(2021, 7, 21), datetime.date(2021, 8, 21)),
                           ('java', datetime.date(2021, 7, 13), datetime.date(2021, 8, 16))
                       ]
                       )

    cursor.executemany('INSERT INTO Student_courses (student_id, course_id) VALUES (?, ?)',
                       [
                           (1, 1),
                           (2, 1),
                           (3, 1),
                           (4, 2)
                       ]
                       )

    # Все студенты, старше 30 лет
    cursor.execute('SELECT * FROM Students WHERE age > 30')
    print(cursor.fetchall())

    # Все студенты, которые проходят курс по python
    cursor.execute("""SELECT name, surname, age, city 
                      FROM Students, Courses, Student_courses 
                      WHERE Students.id = Student_courses.student_id 
                      AND Courses.id = Student_courses.course_id AND course = 'python'""")
    print(cursor.fetchall())

    # Все студенты, которые проходят курс по python и из Spb
    cursor.execute("""SELECT name, surname, age, city 
                      FROM Students, Courses, Student_courses 
                      WHERE Students.id = Student_courses.student_id 
                      AND Courses.id = Student_courses.course_id 
                      AND course = 'python' AND city = 'Spb'""")
    print(cursor.fetchall())
    