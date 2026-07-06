from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class RegisterRequest(BaseModel):
    employee_id: str = Field(..., min_length=3, max_length=30)
    first_name: str
    last_name: str
    email: EmailStr
    phone: Optional[str] = None
    password: str = Field(..., min_length=8)
    organization_id: str
    department_id: Optional[str] = None


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class RefreshTokenRequest(BaseModel):
    refresh_token: str


class ForgotPasswordRequest(BaseModel):
    email: EmailStr


class ResetPasswordRequest(BaseModel):
    token: str
    new_password: str = Field(..., min_length=8)


class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


class UserResponse(BaseModel):
    id: str
    employee_id: str
    first_name: str
    last_name: str
    email: EmailStr
    phone: Optional[str]
    organization_id: str
    department_id: Optional[str]