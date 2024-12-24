# models.py
from sqlalchemy import Column, Integer, String, Date, Text, TIMESTAMP
from sqlalchemy.sql import func
from database import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    date_of_birth = Column(Date, nullable=True)
    phone_number = Column(String(15), nullable=True)
    address = Column(Text, nullable=True)
    enrollment_date = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
