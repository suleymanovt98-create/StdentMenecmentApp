from database import loadStudents, saveStudens


def addStudent():
    students = loadStudents()

    try:
        name = input("enter name: ").strip()
        surname = input("enter surname: ").strip()
        age = int(input("enter age: "))

        grades_input = input("enter grades (məs: 80,90,75): ")
        grades = [int(g.strip()) for g in grades_input.split(",")]

        if not name or not surname:
            print("name and surname cannot be empty!")
            return

        if age < 18:
            print("age must be greater than 17!")
            return

        if not grades or any(grade < 0 or grade > 100 for grade in grades):
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

        if saveStudens(students):
            print("Student added successfully!")

    except ValueError:
        print("please enter numeric value...")

    except (KeyError, TypeError) as e:
        print("Student data error:", e)


def ShowAllStudent():
    students = loadStudents()


def updateStudent():
    pass


def removeStudent():
    pass


def searchStudent():
    pass


if __name__ == "__main__":
    addStudent()
    ShowAllStudent()