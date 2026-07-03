from sqlalchemy import Enum
from sqlalchemy import Index
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from app.models.base_model import BaseModel
from app.core.enums import (
    CompanySizeEnum,
    IndustryEnum,
    StatusEnum,
)


class Organization(BaseModel):
    """
    Organization Master Table
    """
    departments = relationship(
    "Department",
    back_populates="organization",
    cascade="all, delete-orphan",
)
    __tablename__ = "organizations"

    company_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        index=True,
    )

    company_email: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        unique=True,
        index=True,
    )

    phone: Mapped[str | None] = mapped_column(
        String(20),
        nullable=True,
    )

    website: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    industry: Mapped[IndustryEnum] = mapped_column(
        Enum(IndustryEnum),
        nullable=False,
    )

    country: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    state: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    city: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    company_size: Mapped[CompanySizeEnum] = mapped_column(
        Enum(CompanySizeEnum),
        nullable=False,
    )

    gst_number: Mapped[str | None] = mapped_column(
        String(30),
        nullable=True,
        unique=True,
    )

    timezone: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        default="Asia/Kolkata",
    )

    logo_url: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )

    subdomain: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        unique=True,
    )

    status: Mapped[StatusEnum] = mapped_column(
        Enum(StatusEnum),
        nullable=False,
        default=StatusEnum.ACTIVE,
    )

    __table_args__ = (
        Index("idx_company_name", "company_name"),
        Index("idx_company_email", "company_email"),
        Index("idx_subdomain", "subdomain"),
    )