from sqlalchemy import Index
from sqlalchemy import String
from sqlalchemy import Enum as SqlEnum
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.models.base_model import BaseModel
from app.core.enums import StatusEnum


class Role(BaseModel):
    """
    Enterprise Role Table
    """

    __tablename__ = "roles"

    role_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        unique=True,
    )

    description: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )

    status: Mapped[StatusEnum] = mapped_column(
        SqlEnum(StatusEnum),
        nullable=False,
        default=StatusEnum.ACTIVE,
    )

    # Relationship with UserRole
    user_roles = relationship(
        "UserRole",
        back_populates="role",
        cascade="all, delete-orphan",
    )

    # Relationship with RolePermission
    role_permissions = relationship(
        "RolePermission",
        back_populates="role",
        cascade="all, delete-orphan",
    )

    __table_args__ = (
        Index("idx_role_name", "role_name"),
    )