from uuid import UUID

from app import crud
from app.models import Album
from app.models import User
from sqlalchemy.orm import Session

from .base import AuthValidator


class AlbumAuthValidator(AuthValidator):
    @classmethod
    def can_user_add_assets(cls, db: Session, user: User, album: Album) -> bool:

        if cls.is_admin_or_owner(user, album):
            return True

        shared_users = crud.album_user.get_by_album_id(db, album_id=album.id)
        shared_user_ids = [user.id for user in shared_users if user.can_add_assets]

        if user.id in shared_user_ids:
            return True

        return False

    @classmethod
    def can_user_remove_assets(cls, db: Session, user: User, album: Album) -> bool:

        return cls.is_admin_or_owner(user, album)

    # @classmethod
    # def can_user_delete(cls, db: Session, user: User, album: Album) -> bool:
    #     """Can the user delete the album?"""

    #     return cls.is_admin_or_owner(user, album)

    @classmethod
    def can_user_view(cls, db: Session, user: User, album: Album) -> bool:
        """Can the user view photos from the album?"""

        if cls.is_admin_or_owner(user, album):
            return True

        shared_users = crud.album_user.get_by_album_id(db, album_id=album.id)
        shared_user_ids = [user.id for user in shared_users]

        if user.id in shared_user_ids:
            return True

        return False

    @classmethod
    def can_user_edit(cls, db: Session, user: User, album: Album) -> bool:
        """Can the user view photos from the album?"""

        if cls.is_admin_or_owner(user, album):
            return True

        shared_users = crud.album_user.get_by_album_id(db, album_id=album.id)
        shared_user_ids = [user.id for user in shared_users if user.can_edit]

        if user.id in shared_user_ids:
            return True

        return False
