from typing import Any

from app import crud
from app.models import Album
from app.models import User
from sqlalchemy.orm import Session


class AuthValidator:
    @staticmethod
    def is_admin_or_owner(user: User, obj: Any) -> bool:
        if user.is_superuser or user.id == obj.owner_id:
            return True

        return False

    @classmethod
    def can_user_edit(cls, db: Session, user: User, obj: Any) -> bool:
        return cls.is_admin_or_owner(user, obj)

    @classmethod
    def can_user_view(cls, db: Session, user: User, obj: Any) -> bool:
        return cls.is_admin_or_owner(user, obj)

    @classmethod
    def can_user_delete(cls, db: Session, user: User, obj: Any) -> bool:
        return cls.is_admin_or_owner(user, obj)

    @classmethod
    def can_user_create(cls, db: Session, user: User) -> bool:
        return user.is_active
