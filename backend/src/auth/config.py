"""Auth and User Management specific configuration"""

from src.config import settings

SECRET_KEY = settings.SECRET_KEY
JWT_ALGORITHM: str = "HS256"
JWT_LIFETIME_SECONDS: int = 3600  # 1 hour
