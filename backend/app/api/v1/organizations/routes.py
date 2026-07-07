from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.schemas.organization import (
    OrganizationCreate,
    OrganizationResponse,
)
from app.services.organization_service import OrganizationService

router = APIRouter(
    prefix="/organizations",
    tags=["Organizations"],
)


@router.post(
    "/",
    response_model=OrganizationResponse,
    status_code=201,
)
def create_organization(
    request: OrganizationCreate,
    db: Session = Depends(get_db),
):
    service = OrganizationService(db)

    try:
        return service.create(request)

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        )


@router.get(
    "/",
    response_model=list[OrganizationResponse],
)
def get_all_organizations(
    db: Session = Depends(get_db),
):
    service = OrganizationService(db)

    return service.get_all()


@router.get(
    "/{organization_id}",
    response_model=OrganizationResponse,
)
def get_organization(
    organization_id: str,
    db: Session = Depends(get_db),
):
    service = OrganizationService(db)

    try:
        return service.get_by_id(organization_id)

    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e),
        )