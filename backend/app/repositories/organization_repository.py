from typing import Optional

from sqlalchemy.orm import Session

from app.models.organization import Organization


class OrganizationRepository:
    """
    Repository for Organization database operations.
    """

    def __init__(self, db: Session):
        self.db = db

    # ======================================================
    # Create Organization
    # ======================================================

    def create(self, organization: Organization) -> Organization:
        self.db.add(organization)
        self.db.commit()
        self.db.refresh(organization)
        return organization

    # ======================================================
    # Get Organization By ID
    # ======================================================

    def get_by_id(self, organization_id: str) -> Optional[Organization]:
        return (
            self.db.query(Organization)
            .filter(Organization.id == organization_id)
            .first()
        )

    # ======================================================
    # Get Organization By Email
    # ======================================================

    def get_by_email(self, email: str) -> Optional[Organization]:
        return (
            self.db.query(Organization)
            .filter(Organization.company_email == email)
            .first()
        )

    # ======================================================
    # Get Organization By Company Name
    # ======================================================

    def get_by_name(self, company_name: str) -> Optional[Organization]:
        return (
            self.db.query(Organization)
            .filter(Organization.company_name == company_name)
            .first()
        )

    # ======================================================
    # Get Organization By Subdomain
    # ======================================================

    def get_by_subdomain(self, subdomain: str) -> Optional[Organization]:
        return (
            self.db.query(Organization)
            .filter(Organization.subdomain == subdomain)
            .first()
        )

    # ======================================================
    # Get All Organizations
    # ======================================================

    def get_all(self):
        return (
            self.db.query(Organization)
            .order_by(Organization.company_name)
            .all()
        )

    # ======================================================
    # Update Organization
    # ======================================================

    def update(self, organization: Organization) -> Organization:
        self.db.commit()
        self.db.refresh(organization)
        return organization

    # ======================================================
    # Delete Organization
    # ======================================================

    def delete(self, organization: Organization):
        self.db.delete(organization)
        self.db.commit()