from sqlalchemy.orm import Session

from app.models.organization import Organization
from app.repositories.organization_repository import OrganizationRepository
from app.schemas.organization import (
    OrganizationCreate,
)


class OrganizationService:
    """
    Business logic for Organization.
    """

    def __init__(self, db: Session):
        self.db = db
        self.repository = OrganizationRepository(db)

    # ====================================================
    # Create Organization
    # ====================================================

    def create(
        self,
        request: OrganizationCreate,
    ) -> Organization:

        # Check company email
        if self.repository.get_by_email(
            request.company_email
        ):
            raise ValueError(
                "Company email already exists."
            )

        # Check subdomain
        if self.repository.get_by_subdomain(
            request.subdomain
        ):
            raise ValueError(
                "Subdomain already exists."
            )

        organization = Organization(

            company_name=request.company_name,

            company_email=request.company_email,

            phone=request.phone,

            website=request.website,

            industry=request.industry,

            country=request.country,

            state=request.state,

            city=request.city,

            company_size=request.company_size,

            gst_number=request.gst_number,

            timezone=request.timezone,

            subdomain=request.subdomain,
        )

        return self.repository.create(
            organization
        )

    # ====================================================
    # Get Organization
    # ====================================================

    def get_by_id(
        self,
        organization_id: str,
    ):

        organization = self.repository.get_by_id(
            organization_id
        )

        if organization is None:

            raise ValueError(
                "Organization not found."
            )

        return organization

    # ====================================================
    # Get All
    # ====================================================

    def get_all(self):

        return self.repository.get_all()