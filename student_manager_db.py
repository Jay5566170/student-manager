import sqlite3

# ----- DATABASE SETUP -----
# This runs once when the program starts
connection = sqlite3.connect("students.db")
cursor = connection.cursor()

# Create the table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    city TEXT NOT NULL,
    email TEXT
)
""")
connection.commit()

# ----- CORE FUNCTIONS -----

def add_student():
    """Insert a new student into the database."""
    name = input("Name: ").strip()
    age = int(input("Age: "))
    city = input("City: ").strip()
    email = input("Email: ").strip()

    cursor.execute(
        "INSERT INTO students (name, age, city, email) VALUES (?, ?, ?, ?)",
        (name, age, city, email)
    )
    connection.commit()
    print(f"✅ {name} added successfully!\n")


def show_students():
    """Display all students in the database."""
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    if not students:
        print("📭 No students found.\n")
        return

    print("\n📋 All Students:")
    for student in students:
        print(f"  ID: {student[0]} | Name: {student[1]} | Age: {student[2]} | City: {student[3]} | Email: {student[4]}")
    print()


def find_student():
    """Search for a student by name."""
    name = input("Enter student name to search: ").strip()

    cursor.execute("SELECT * FROM students WHERE name = ?", (name,))
    student = cursor.fetchone()

    if student:
        print(f"✅ Found: ID: {student[0]} | Name: {student[1]} | Age: {student[2]} | City: {student[3]} | Email: {student[4]}\n")
    else:
        print(f"❌ No student found with name '{name}'.\n")


def show_adults():
    """Display all students aged 18 or older."""
    cursor.execute("SELECT * FROM students WHERE age >= 18")
    adults = cursor.fetchall()

    if not adults:
        print("📭 No adults (18+) found.\n")
        return

    print("\n🧑 Adults (18+):")
    for student in adults:
        print(f"  ID: {student[0]} | Name: {student[1]} | Age: {student[2]} | City: {student[3]} | Email: {student[4]}")
    print()


def delete_student():
    """Delete a student by ID."""
    student_id = input("Enter student ID to delete: ").strip()

    # Check if student exists
    cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
    student = cursor.fetchone()

    if not student:
        print(f"❌ No student found with ID '{student_id}'.\n")
        return

    confirm = input(f"⚠️ Are you sure you want to delete {student[1]}? (y/n): ").lower()
    if confirm == 'y':
        cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
        connection.commit()
        print(f"✅ Student deleted successfully!\n")
    else:
        print("❌ Deletion cancelled.\n")


# ----- MAIN MENU -----

def main():
    while True:
        print("\n===== STUDENT MANAGER (SQLite) =====")
        print("1. Add student")
        print("2. Show students")
        print("3. Find student")
        print("4. Show adults (18+)")
        print("5. Delete student")
        print("6. Exit")
        print("====================================")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            show_students()
        elif choice == "3":
            find_student()
        elif choice == "4":
            show_adults()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid option. Please try again.\n")

    # Close the database connection when the program ends
    connection.close()


# ----- RUN THE PROGRAM -----
if __name__ == "__main__":
    main()