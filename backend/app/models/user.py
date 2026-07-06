from datetime import datetime
from sqlalchemy import Boolean
from sqlalchemy import Date
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Index
from sqlalchemy import String
from sqlalchemy import Enum as SqlEnum
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.models.base_model import BaseModel
from app.core.enums import StatusEnum


class User(BaseModel):

    __tablename__ = "users"

    organization_id: Mapped[str] = mapped_column(
        ForeignKey("organizations.id"),
        nullable=False,
        index=True,
    )
    department_id: Mapped[str | None] = mapped_column(
    ForeignKey("departments.id"),
    nullable=True,
    index=True,
    )
    employee_id: Mapped[str] = mapped_column(
        String(30),
        unique=True,
        nullable=False,
    )
    first_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    last_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    date_of_birth: Mapped[Date | None] = mapped_column(
        Date,
        nullable=True,
    )

    gender: Mapped[str | None] = mapped_column(
        String(20),
        nullable=True,
    )   
    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False,
        index=True,
    )

    phone: Mapped[str | None] = mapped_column(
        String(20),
        nullable=True,
    )
    password_hash: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )
    profile_image: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )
    email_verified: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )
    last_login: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
    )
    status: Mapped[StatusEnum] = mapped_column(
        SqlEnum(StatusEnum),
        default=StatusEnum.ACTIVE,
    )
    organization = relationship(
        "Organization",
        back_populates="users",
    )

    department = relationship(
        "Department",
        back_populates="users",
    )
    user_roles = relationship(
    "UserRole",
    back_populates="user",
    cascade="all, delete-orphan",
    )
    __table_args__ = (

        Index("idx_user_email", "email"),

        Index("idx_employee_id", "employee_id"),

    )