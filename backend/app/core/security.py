from datetime import datetime, timedelta, timezone
from typing import Any

from jose import JWTError, jwt
# pyrefly: ignore [missing-import]
from passlib.context import CryptContext

from app.core.config import settings

# =====================================================
# Password Hashing
# =====================================================

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

# =====================================================
# Password Functions
# =====================================================

def hash_password(password: str) -> str:
    """
    Hash plain password.
    """
    return pwd_context.hash(password)


def verify_password(
    plain_password: str,
    hashed_password: str
) -> bool:
    """
    Verify password.
    """
    return pwd_context.verify(
        plain_password,
        hashed_password
    )


# =====================================================
# JWT Token Creation
# =====================================================

def create_access_token(
    subject: str,
    expires_minutes: int | None = None
) -> str:

    if expires_minutes is None:
        expires_minutes = settings.ACCESS_TOKEN_EXPIRE_MINUTES

    expire = datetime.now(timezone.utc) + timedelta(
        minutes=expires_minutes
    )

    payload = {
        "sub": subject,
        "exp": expire,
        "type": "access"
    }

    encoded = jwt.encode(
        payload,
        settings.JWT_SECRET_KEY,
        algorithm=settings.JWT_ALGORITHM
    )

    return encoded


def create_refresh_token(
    subject: str
) -> str:

    expire = datetime.now(timezone.utc) + timedelta(
        days=settings.REFRESH_TOKEN_EXPIRE_DAYS
    )

    payload = {
        "sub": subject,
        "exp": expire,
        "type": "refresh"
    }

    encoded = jwt.encode(
        payload,
        settings.JWT_SECRET_KEY,
        algorithm=settings.JWT_ALGORITHM
    )

    return encoded


# =====================================================
# Decode JWT
# =====================================================

def decode_token(
    token: str
) -> dict[str, Any]:

    try:

        payload = jwt.decode(
            token,
            settings.JWT_SECRET_KEY,
            algorithms=[settings.JWT_ALGORITHM]
        )

        return payload

    except JWTError:

        raise ValueError("Invalid Token")