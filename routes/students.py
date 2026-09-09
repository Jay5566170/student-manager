from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from models import Student
from schemas import StudentCreate, StudentUpdate, StudentResponse
from auth import get_current_user

router = APIRouter(prefix="/students", tags=["students"])

# GET all students (protected)
@router.get("/", response_model=List[StudentResponse])
def get_all_students(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)  # 👈 Add this!
):
    students = db.query(Student).all()
    return students

# GET one student (protected)
@router.get("/{student_id}", response_model=StudentResponse)
def get_student(
    student_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)  # 👈 Add this!
):
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

# POST create student (protected)
@router.post("/", response_model=StudentResponse)
def create_student(
    student: StudentCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)  # 👈 Add this!
):
    db_student = Student(
        name=student.name,
        age=student.age,
        city=student.city,
        email=student.email,
        created_by=current_user.id  # 👈 Track who created it
    )
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

# PUT update student (protected)
@router.put("/{student_id}", response_model=StudentResponse)
def update_student(
    student_id: int,
    student_update: StudentUpdate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)  # 👈 Add this!
):
    db_student = db.query(Student).filter(Student.id == student_id).first()
    if not db_student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    if student_update.name is not None:
        db_student.name = student_update.name
    if student_update.age is not None:
        db_student.age = student_update.age
    if student_update.city is not None:
        db_student.city = student_update.city
    if student_update.email is not None:
        db_student.email = student_update.email
    
    db.commit()
    db.refresh(db_student)
    return db_student

# DELETE student (protected)
@router.delete("/{student_id}")
def delete_student(
    student_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)  # 👈 Add this!
):
    db_student = db.query(Student).filter(Student.id == student_id).first()
    if not db_student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    db.delete(db_student)
    db.commit()
    return {"message": f"Student {student_id} deleted successfully"}