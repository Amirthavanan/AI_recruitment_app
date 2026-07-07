from fastapi import Depends
from fastapi import HTTPException
from fastapi import status

from fastapi.security import OAuth2PasswordBearer

from jose import JWTError

from sqlalchemy.orm import Session

from app.core.security import decode_token

from app.database.dependencies import get_db

from app.repositories.user_repository import UserRepository


oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login"
)


def get_current_user(

    token: str = Depends(oauth2_scheme),

    db: Session = Depends(get_db),

):

    credentials_exception = HTTPException(

        status_code=status.HTTP_401_UNAUTHORIZED,

        detail="Could not validate credentials",

        headers={"WWW-Authenticate": "Bearer"},

    )

    try:

        payload = decode_token(token)

        user_id = payload.get("sub")

        if user_id is None:
            raise credentials_exception

    except JWTError:

        raise credentials_exception

    repository = UserRepository(db)

    user = repository.get_by_id(user_id)

    if user is None:

        raise credentials_exception

    return user