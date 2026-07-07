from typing import Optional

from pydantic import BaseModel, ConfigDict, EmailStr, Field


# ==========================================================
# Register
# ==========================================================

class RegisterRequest(BaseModel):
    employee_id: str = Field(..., min_length=3, max_length=30)
    first_name: str = Field(..., min_length=2, max_length=100)
    last_name: str = Field(..., min_length=2, max_length=100)
    email: EmailStr
    phone: Optional[str] = Field(default=None, max_length=20)
    password: str = Field(..., min_length=8)
    organization_id: str
    department_id: Optional[str] = None


# ==========================================================
# Login
# ==========================================================

class LoginRequest(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8)


# ==========================================================
# Refresh Token
# ==========================================================

class RefreshTokenRequest(BaseModel):
    refresh_token: str


# ==========================================================
# Forgot Password
# ==========================================================

class ForgotPasswordRequest(BaseModel):
    email: EmailStr


# ==========================================================
# Reset Password
# ==========================================================

class ResetPasswordRequest(BaseModel):
    token: str
    new_password: str = Field(..., min_length=8)


# ==========================================================
# Change Password
# ==========================================================

class ChangePasswordRequest(BaseModel):
    current_password: str
    new_password: str = Field(..., min_length=8)


# ==========================================================
# JWT Token Response
# ==========================================================

class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


# ==========================================================
# User Response
# ==========================================================

class UserResponse(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    id: str
    employee_id: str
    first_name: str
    last_name: str
    email: EmailStr
    phone: Optional[str]
    organization_id: str
    department_id: Optional[str]
    email_verified: bool
    status: str


# ==========================================================
# Login Response
# ==========================================================

class LoginResponse(BaseModel):
    user: UserResponse
    token: TokenResponse