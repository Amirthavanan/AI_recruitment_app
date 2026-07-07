from sqlalchemy.orm import Session

from app.core.security import (
    hash_password,
    verify_password,
    create_access_token,
    create_refresh_token,
)
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.auth import (
    RegisterRequest,
    LoginRequest,
    TokenResponse,
)


class AuthService:

    def __init__(self, db: Session):
        self.db = db
        self.user_repository = UserRepository(db)

    # ===================================================
    # Register User
    # ===================================================

    def register(self, request: RegisterRequest):

        existing_email = self.user_repository.get_by_email(request.email)

        if existing_email:
            raise ValueError("Email already exists.")

        existing_employee = self.user_repository.get_by_employee_id(
            request.employee_id
        )

        if existing_employee:
            raise ValueError("Employee ID already exists.")

        user = User(
            employee_id=request.employee_id,
            first_name=request.first_name,
            last_name=request.last_name,
            email=request.email,
            phone=request.phone,
            password_hash=hash_password(request.password),
            organization_id=request.organization_id,
            department_id=request.department_id,
        )

        return self.user_repository.create(user)

    # ===================================================
    # Login
    # ===================================================

    def login(self, request: LoginRequest) -> TokenResponse:

        user = self.user_repository.get_by_email(request.email)

        if user is None:
            raise ValueError("Invalid email or password.")

        if not verify_password(
            request.password,
            user.password_hash,
        ):
            raise ValueError("Invalid email or password.")

        access_token = create_access_token(str(user.id))

        refresh_token = create_refresh_token(str(user.id))

        return TokenResponse(
            access_token=access_token,
            refresh_token=refresh_token,
        )