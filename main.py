from fastapi import FastAPI, HTTPException
import sqlite3
from pydantic import BaseModel
from typing import Optional

app = FastAPI(
    title="Student Manager API",
    description="Complete CRUD API for students",
    version="1.0.0"
)

# Pydantic models
class StudentCreate(BaseModel):
    name: str
    age: int
    city: str
    email: Optional[str] = None

class StudentUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    city: Optional[str] = None
    email: Optional[str] = None

# Database helper
def get_connection():
    conn = sqlite3.connect("students.db")
    conn.row_factory = sqlite3.Row
    return conn

# GET /students — get all students
@app.get("/students")
def get_all_students():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    conn.close()
    return {"students": [dict(row) for row in students]}

# GET /students/{id} — get one student
@app.get("/students/{student_id}")
def get_student(student_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
    student = cursor.fetchone()
    conn.close()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return dict(student)

# POST /students — create a new student
@app.post("/students")
def create_student(student: StudentCreate):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO students (name, age, city, email) VALUES (?, ?, ?, ?)",
        (student.name, student.age, student.city, student.email)
    )
    conn.commit()
    student_id = cursor.lastrowid
    conn.close()
    
    return {
        "id": student_id,
        "name": student.name,
        "age": student.age,
        "city": student.city,
        "email": student.email
    }

# PUT /students/{id} — update a student
@app.put("/students/{student_id}")
def update_student(student_id: int, student_update: StudentUpdate):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
    existing = cursor.fetchone()
    if not existing:
        conn.close()
        raise HTTPException(status_code=404, detail="Student not found")
    
    updates = []
    values = []
    
    if student_update.name is not None:
        updates.append("name = ?")
        values.append(student_update.name)
    if student_update.age is not None:
        updates.append("age = ?")
        values.append(student_update.age)
    if student_update.city is not None:
        updates.append("city = ?")
        values.append(student_update.city)
    if student_update.email is not None:
        updates.append("email = ?")
        values.append(student_update.email)
    
    if not updates:
        conn.close()
        raise HTTPException(status_code=400, detail="No fields to update")
    
    values.append(student_id)
    query = f"UPDATE students SET {', '.join(updates)} WHERE id = ?"
    cursor.execute(query, values)
    conn.commit()
    conn.close()
    
    return {"message": f"Student {student_id} updated successfully"}

# DELETE /students/{id} — delete a student
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
    existing = cursor.fetchone()
    if not existing:
        conn.close()
        raise HTTPException(status_code=404, detail="Student not found")
    
    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    conn.close()
    
    return {"message": f"Student {student_id} deleted successfully"}

@app.get("/")
def root():
    return {"message": "Student Manager API is running", "docs": "/docs"}