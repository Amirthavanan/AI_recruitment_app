from typing import Optional

from sqlalchemy.orm import Session

from app.models.user import User


class UserRepository:
    """
    Repository class for User database operations.
    """

    def __init__(self, db: Session):
        self.db = db

    # -----------------------------
    # Create User
    # -----------------------------
    def create(self, user: User) -> User:
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    # -----------------------------
    # Get User By ID
    # -----------------------------
    def get_by_id(self, user_id: str) -> Optional[User]:
        return (
            self.db.query(User)
            .filter(User.id == user_id)
            .first()
        )

    # -----------------------------
    # Get User By Email
    # -----------------------------
    def get_by_email(self, email: str) -> Optional[User]:
        return (
            self.db.query(User)
            .filter(User.email == email)
            .first()
        )

    # -----------------------------
    # Get User By Employee ID
    # -----------------------------
    def get_by_employee_id(self, employee_id: str) -> Optional[User]:
        return (
            self.db.query(User)
            .filter(User.employee_id == employee_id)
            .first()
        )

    # -----------------------------
    # Get All Users
    # -----------------------------
    def get_all(self):
        return (
            self.db.query(User)
            .all()
        )

    # -----------------------------
    # Update User
    # -----------------------------
    def update(self, user: User) -> User:
        self.db.commit()
        self.db.refresh(user)
        return user

    # -----------------------------
    # Delete User
    # -----------------------------
    def delete(self, user: User):
        self.db.delete(user)
        self.db.commit()