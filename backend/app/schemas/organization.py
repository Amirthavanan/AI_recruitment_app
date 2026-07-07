from pydantic import BaseModel, ConfigDict, EmailStr, Field


class OrganizationCreate(BaseModel):

    company_name: str = Field(..., min_length=2, max_length=200)

    company_email: EmailStr

    phone: str

    website: str | None = None

    industry: str

    country: str

    state: str

    city: str

    company_size: str

    gst_number: str | None = None

    timezone: str

    subdomain: str


class OrganizationResponse(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    id: str

    company_name: str

    company_email: EmailStr

    phone: str

    website: str | None

    industry: str

    country: str

    state: str

    city: str

    company_size: str

    timezone: str

    subdomain: str

    status: str