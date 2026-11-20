import student

def ShowAllStudent():
    students = loadStudents()

    if len(students) == 0:
        print("Student yoxdur!")
        return

    for student in students:
        print(student["id"], student["name"], student["surname"], student["age"], student["grades"])


while True:
    print("")
    print("1 - Add student")
    print("2 - Show all students")
    print("3 - Update student")
    print("4 - Remove student")
    print("5 - Search student")
    print("0 - Exit")

    secim = input("Choose: ")

    if secim == "1":
        addStudent()
    elif secim == "2":
        ShowAllStudent()
    elif secim == "3":
        updateStudent()
    elif secim == "4":
        removeStudent()
    elif secim == "5":
        searchStudent()
    elif secim == "0":
        print("sagolun")
        break
    else:
        print("Wrong choice!")

