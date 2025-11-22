
from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True

# Đầu vào: kiểm tra email hợp lệ
class UserInput(BaseModel):
    email: EmailStr

# Đầu ra: kiểm tra dữ liệu trả về
class UserOutput(BaseModel):
    id: int
    email: EmailStr
    is_active: bool