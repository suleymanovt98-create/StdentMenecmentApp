from database import *


def addStudent():
    students = loadStudents()
 
    try:
        name = input("enter name: ").strip()
        surname = input("enter name: ").strip()
        age = int(input("enter name: "))
 
        grades = input("enter grades: ")
        grades = [int(grades.strip()) for grades in grades.split(",")]
 
        if not name or not surname:
            print("name and surname cannot be empty!")
            return
 
        if age < 17:
            print("age must be greater than 17!")
            return
 
        if not grades or any(grade < 0 and grade > 100 for grade in grades):
            print("grades must be between 0 and 100!")
            return
 
        newStudent = {
            "id": max([student["id"] for student in students], default=0) + 1,
            "name": name,
            "surname": surname,
            "age": age,
            "grades": grades
        }
 
        students.append(newStudent)
 
        if saveStudents(students):
            print("Student added successfully!")
 
    except ValueError:
        print("please enter numeric value...")
 
    except (KeyError, TypeError) as e:
        print("Student data error:", e)

def ShowAllStudent():
    pass

def updateStudent():
    pass


def removeStudent():
    pass

def searchStudent():
    pass