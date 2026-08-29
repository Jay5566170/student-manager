import json
import os


def load_students():
    if os.path.exists("students.json"):
        with open("students.json", "r") as file:
            return json.load(file)

    return []


def save_students():
    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)


def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))

    student = {
        "name": name,
        "age": age
    }

    students.append(student)

    print("Student added successfully!")


def show_students():
    if len(students) == 0:
        print("No students found.")
        return

    print("\n--- Students ---")

    for student in students:
        print(f"Name: {student['name']}, Age: {student['age']}")


def find_student():
    name = input("Enter student name to find: ")

    for student in students:
        if student["name"].lower() == name.lower():
            print(f"Found: {student['name']}, Age: {student['age']}")
            return

    print("Student not found.")


def show_adults():
    print("\n--- Adult Students ---")

    found = False

    for student in students:
        if student["age"] >= 18:
            print(f"Name: {student['name']}, Age: {student['age']}")
            found = True

    if not found:
        print("No adult students found.")


def menu():
    while True:
        print("\n===== STUDENT MANAGER =====")
        print("1. Add student")
        print("2. View students")
        print("3. Find student")
        print("4. Show adults")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            show_students()

        elif choice == "3":
            find_student()

        elif choice == "4":
            show_adults()

        elif choice == "5":
            print("Saving students...")
            break

        else:
            print("Invalid choice. Please try again.")


students = load_students()

menu()

save_students()

print("Students saved. Goodbye!")