import sqlite3
import faker
from random import randint, choice
from datetime import datetime
from pprint import pprint
fake = faker.Faker()

BASE = "college.db"
STUDENTS = 70
TEACHERS = 5
GROUPS = ["СБУ-14","ПГС-13","АРХ-12"]
SUBJECTS = [
    "English Language",
    "Mathematic",
    "History",
    "Programming",
    "Biology",
    "Physics",
    "Chemistry",
    "Astronomy",
    "Ukrainian Language",
    "Design",
    "Spain Language",
    "Geography",
    "Geometry",
    "French Language"



    ]


def seed_students():
    students_prepare = [fake.name() for i in range(STUDENTS)]
    groups = [randint(1,3) for i in range(0, STUDENTS)]
    students_to_sql = zip(students_prepare, groups)

    sqlScript = '''
    INSERT INTO students(fullname, group_id)
    VALUES(?,?);
    '''
    with sqlite3.connect(BASE) as connect:
        cursor = connect.cursor()
        cursor.executemany(sqlScript, students_to_sql)

        cursor.close()
    connect.close()

def seed_groups():
    sqlScript = '''
    INSERT INTO ggroups(name)
    VALUES(?)
    '''
    with sqlite3.connect(BASE) as connect:
        cursor = connect.cursor()
        for i in GROUPS:
            cursor.execute(sqlScript,(i,))
        
        cursor.close()
    connect.close()

def seed_teachers():
    sqlScript = '''
    INSERT INTO teachers(fullname)
    VALUES(?);
    '''
    teachers = [fake.name() for i in range(TEACHERS)]
    with sqlite3.connect(BASE) as connect:
        cursor = connect.cursor()
        for i in teachers:
            cursor.execute(sqlScript,(i,))
        cursor.close()
    connect.close()

def seed_subjects():
    sqlScript = '''
    INSERT INTO subjects(name, teacher_id)
    VALUES (?,?);
    '''
    teachers = [(i, randint(1,TEACHERS)) for i in SUBJECTS]
    with sqlite3.connect(BASE) as connect:
        cursor = connect.cursor()
        cursor.executemany(sqlScript,teachers)
        cursor.close()

    connect.close()

def seed_grades():
    




































