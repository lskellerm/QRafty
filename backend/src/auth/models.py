"""Database models associated with User management"""

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from fastapi_users.db import SQLAlchemyBaseUserTableUUID
from ..database import Base


class User(SQLAlchemyBaseUserTableUUID, Base):
    """
    User model for the database, extends the SQLAlchemyBaseUserTableUUID and the Base class

    Args:
        SQLAlchemyBaseUserTableUUID (SQLAlchemyBaseUserTableUUID): Base class for the User model, provided by fastapi_users
        Base (DecarativeBase): Base class for all SQLAlchemy database models
    """

    name: Mapped[str] = mapped_column(String(30), nullable=False)
    username: Mapped[str] = mapped_column(String(30), nullable=False, unique=True)
