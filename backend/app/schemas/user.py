from pydantic import BaseModel, EmailStr
from app.models.user import UserRole

class UserRegister(BaseModel):
    email: EmailStr
    password: str
    full_name: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    email: str
    full_name: str
    role: UserRole
    is_verified: bool

    class Config:
        from_attributes = True   

class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"