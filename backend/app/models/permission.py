from sqlalchemy import Enum as SqlEnum
from sqlalchemy import Index
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.core.enums import StatusEnum
from app.models.base_model import BaseModel


class Permission(BaseModel):
    """
    Enterprise Permission Model

    Stores all application permissions.
    Example:
        USER_CREATE
        USER_UPDATE
        JOB_CREATE
        JOB_APPROVE
    """

    __tablename__ = "permissions"

    permission_code: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        unique=True,
    )

    permission_name: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )

    module_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
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

    role_permissions = relationship(
        "RolePermission",
        back_populates="permission",
        cascade="all, delete-orphan",
    )

    __table_args__ = (
        Index("idx_permission_code", "permission_code"),
        Index("idx_permission_module", "module_name"),
    )

    def __repr__(self):
        return f"<Permission {self.permission_code}>"