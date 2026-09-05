from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Student Manager API is running"}


students = [
    {"id": 1, "name": "Ali", "age": 21, "city": "Lahore"},
    {"id": 2, "name": "Ahmed", "age": 23, "city": "Islamabad"},
]


@app.get("/students")
def get_students():
    return students


@app.get("/students/{student_id}")
def get_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            return student

    return {"message": "Student not found"}