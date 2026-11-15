import json

def loadStudents():
    try:
        with open("students.json", "r", encoding="utf-8") as f:
            students = json.load(f)


        return students

    except FileNotFoundError as e:
        print(e)
        return[]

    except json.JSONDecodeError as e:
        print(e)
        return[]