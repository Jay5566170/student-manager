from pydantic import BaseModel
from typing import Optional

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

class StudentResponse(BaseModel):
    id: int
    name: str
    age: int
    city: str
    email: Optional[str]
    
    class Config:
        orm_mode = True