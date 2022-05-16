
from uuid import UUID

from app import crud
from app.models import Album
from app.models import User
from sqlalchemy.orm import Session


class AlbumAuthValidator:

    @classmethod
    def can_user_add_assets(db: Session, user: User , album: Album) -> bool:

        if user.is_superuser or user.id == album.owner_id:
            return True

        shared_users = crud.album_user.get_by_album_id(db, album_id=album.id)
        shared_user_ids = [user.id for user in shared_users if user.can_add_assets]

        if user.id in shared_user_ids:
            return True

        return False

    @classmethod
    def can_user_remove_assets(db: Session, user: User , album: Album) -> bool:
        
        if user.is_superuser or user.id == album.owner_id:
            return True

        
        return False

    @classmethod
    def can_user_delete(db: Session, user: User , album: Album) -> bool:
        """ Can the user delete the album? """

        if user.is_superuser or user.id == album.owner_id:
            return True

        return False

    @classmethod
    def can_user_view(db: Session, user: User , album: Album) -> bool:
        """ Can the user view photos from the album? """

        if user.is_superuser or user.id == album.owner_id:
            return True

        shared_users = crud.album_user.get_by_album_id(db, album_id=album.id)
        shared_user_ids = [user.id for user in shared_users]

        if user.id in shared_user_ids:
            return True

        return False
