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

    students = loadStudents()

    try:
        student_id = int(input("enter student id: "))

        for student in students:
            if student["id"] == student_id:
                name = input("new name: ")
                surname = input("new surname: ")
                age = int(input("new age: "))
                grades = input("new grades: ")
                grades = [int(g) for g in grades.split(",")]

                student["name"] = name
                student["surname"] = surname
                student["age"] = age
                student["grades"] = grades

                saveStudens(students)
                print("Student update")
                return

        print("Student not found!")

    except ValueError:
        print("please enter numeric value")


def removeStudent():
    students = loadStudents()

    try:
        student_id = int(input("enter student id: "))

        for student in students:
            if student["id"] == student_id:
                students.remove(student)
                saveStudens(students)
                print("Student remove")
                return

        print("Student not found!")

    except ValueError:
        print("please enter numeric value")


def searchStudent():
    students = loadStudents()

    try:
        keyword = input("enter name: ").lower()
        found = False

        for student in students:
            if keyword in student["name"].lower():
                print(student["id"], student["name"], student["surname"], student["age"], student["grades"])
                found = True

        if not found:
            print("Student not found")

    except KeyError:
        print("student data error")


if __name__ == "__main__":
    addStudent()
    ShowAllStudent()