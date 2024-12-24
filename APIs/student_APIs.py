# main.py
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database.database import get_db
from database.models import Student
from database.schema import StudentCreate, StudentUpdate

app = FastAPI()


@app.post("/students/", response_model=dict)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    new_student = Student(**student.dict())
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return {"message": "Student created successfully", "student": student.dict()}


@app.put("/students/{student_id}", response_model=dict)
def update_student(student_id: int, student: StudentUpdate, db: Session = Depends(get_db)):
    existing_student = db.query(Student).filter(Student.id == student_id).first()
    if not existing_student:
        raise HTTPException(status_code=404, detail="Student not found")
    for key, value in student.dict(exclude_unset=True).items():
        setattr(existing_student, key, value)
    db.commit()
    db.refresh(existing_student)
    return {"message": "Student updated successfully", "student": existing_student}


@app.delete("/students/{student_id}", response_model=dict)
def delete_student(student_id: int, db: Session = Depends(get_db)):
    student_to_delete = db.query(Student).filter(Student.id == student_id).first()
    if not student_to_delete:
        raise HTTPException(status_code=404, detail="Student not found")
    db.delete(student_to_delete)
    db.commit()
    return {"message": "Student deleted successfully"}


@app.get("/students/search", response_model=dict)
def search_students(
        student_id: int = None,
        name: str = None,
        db: Session = Depends(get_db)
):
    """
    Search for students by ID or name.
    """
    if not student_id and not name:
        raise HTTPException(
            status_code=400,
            detail="At least one search parameter (student_id or name) must be provided."
        )

    query = db.query(Student)

    if student_id:
        student = query.filter(Student.id == student_id).first()
        if not student:
            raise HTTPException(status_code=404, detail="Student with the given ID not found")
        return {"message": "Student found", "student": student}

    if name:
        students = query.filter(Student.name.ilike(f"%{name}%")).all()
        if not students:
            raise HTTPException(status_code=404, detail="No students found with the given name")
        return {"message": f"Found {len(students)} students", "students": students}

