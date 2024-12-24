# schemas.py
from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date


class StudentCreate(BaseModel):
    name: str
    email: EmailStr
    date_of_birth: Optional[date] = None
    phone_number: Optional[str] = None
    address: Optional[str] = None


class StudentUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    date_of_birth: Optional[date] = None
    phone_number: Optional[str] = None
    address: Optional[str] = None
