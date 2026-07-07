from fastapi import APIRouter

from fastapi import Depends

from app.core.dependencies import get_current_user

from app.models.user import User

router = APIRouter(

    prefix="/users",

    tags=["Users"]

)


@router.get("/me")

def me(

    current_user: User = Depends(get_current_user)

):

    return current_user