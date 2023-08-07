from peewee import *
import datetime

# подключаемся к базе данных или создаем в случае ее отсутствия
db = SqliteDatabase('db_20-50_07-08-2023.sqlite')

# базовая модель чтоб не повторяться
class BaseModel(Model):
    # метакласс который хранит ссылку на базу данных
    class Meta:
        database = db

# модель таблицы
class Students(BaseModel):
    id = PrimaryKeyField(unique=True)
    name = CharField(max_length=32)
    surname = CharField(max_length=32)
    age = IntegerField()
    city = CharField(max_length=32)

class Courses(BaseModel):
    id = PrimaryKeyField(unique=True)
    name = CharField(max_length=32)
    time_start = DateField()
    time_end = DateField()

class Student_courses(BaseModel):
    student_id = ForeignKeyField(Students)
    course_id = ForeignKeyField(Courses)

with db:
    db.create_tables([Students, Courses, Student_courses])

    Students.insert_many([
        {'name': 'Max', 'surname': 'Brooks', 'age': 24, 'city': 'Spb'},
        {'name': 'John', 'surname': 'Stones', 'age': 15, 'city': 'Spb'},
        {'name': 'Andy', 'surname': 'Wings', 'age': 45, 'city': 'Manhester'},
        {'name': 'Kate', 'surname': 'Brooks', 'age': 34, 'city': 'Spb'}]
    ).execute()

    Courses.insert_many([
        {'name': 'python', 'time_start': datetime.date(2021, 7, 21), 'time_end': datetime.date(2021, 8, 21)},
        {'name': 'java', 'time_start': datetime.date(2021, 7, 13), 'time_end': datetime.date(2021, 8, 16)}]
    ).execute()

    Student_courses.insert_many([
        {'student_id': 1, 'course_id': 1},
        {'student_id': 2, 'course_id': 1},
        {'student_id': 3, 'course_id': 1},
        {'student_id': 4, 'course_id': 2}]
    ).execute()

    # Все студенты, старше 30 лет
    students = Students.select().where(Students.age > 30)
    for student in students:
        print(f'name: {student.name}, surname: {student.surname}, age: {student.age}, city: {student.city}')

    print()

    # Все студенты, которые проходят курс по python
    students = (Students.select().join(Student_courses).join(Courses).where(Courses.name == 'python'))
    for student in students:
        print(f'name: {student.name}, surname: {student.surname}, age: {student.age}, city: {student.city}')

    print()

    # Все студенты, которые проходят курс по python и из Spb
    students = (Students
                .select()
                .join(Student_courses)
                .join(Courses)
                .where(Courses.name == 'python')
                .where(Students.city == 'Spb'))
    for student in students:
        print(f'name: {student.name}, surname: {student.surname}, age: {student.age}, city: {student.city}')
