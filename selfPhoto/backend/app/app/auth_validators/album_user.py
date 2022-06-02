from app import crud
from app.auth_validators import album
from app.models import Album
from app.models import User
from app.schemas import AlbumUser
from sqlalchemy.orm import Session

from .base import AuthValidator


class AlbumUserAuthValidator(AuthValidator):
    @classmethod
    def can_user_view(cls, db: Session, user: User, album: Album) -> bool:
        """Can the user view album_users?"""

        if cls.is_admin_or_owner(user, album):
            return True

        shared_users = crud.album_user.get_by_album_id(db, album_id=album.id)
        shared_user_ids = [user.user_id for user in shared_users]

        if user.id in shared_user_ids:
            return True

        return False

    @classmethod
    def can_user_delete(
        cls, db: Session, user: User, album: Album, album_user: AlbumUser
    ) -> bool:
        if cls.is_admin_or_owner(user, album):
            return True

        if album_user.user_id == user.id:
            return True

        return False

    @classmethod
    def can_user_create(cls, db: Session, user: User, album: Album) -> bool:
        if cls.is_admin_or_owner(user, album):
            return True

        shared_users = crud.album_user.get_by_album_id(db, album_id=album.id)
        shared_user_ids = [
            user.user_id for user in shared_users if user.can_share_album
        ]

        if user.id in shared_user_ids:
            return True

        return False

    @classmethod
    def can_user_edit(cls, db: Session, user: User, obj: Album) -> bool:
        if cls.is_admin_or_owner(user, obj):
            return True

        return False
