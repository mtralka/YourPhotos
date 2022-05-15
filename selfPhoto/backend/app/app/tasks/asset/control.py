from pathlib import Path
from typing import Any

from app import crud
from app.core.config import GeocodingService
from app.core.config import settings
from app.core.huey_app import huey
from app.db.session import SessionLocal
from app.models import Asset
from app.models import Exif
from app.models import Geocode
from app.schemas import AssetUpdate
from app.schemas import ExifCreate
from app.schemas import GeocodeCreate

from .exif import extract_exif_data
from .geocode import geocode
from .thumbnail import generate_thumbnail
from uuid import UUID

# db = SessionLocal()


@huey.task()
def process_asset(asset_id: UUID):

    # db = SessionLocal()

    with SessionLocal() as db:
        # Asset
        # tasks: list = []

        asset: Asset | None = crud.asset.get_by_id(db=db, id=asset_id)

        if not asset:
            print("FAILED")
            return

        asset_path: Path = Path(asset.asset_path)

        while not asset_path.exists():
            print("WAITING")

        ##
        # Check if asset already exists (dedupe)
        ##
        # this should be blocking

        ##
        # Generate thumbnail
        ##
        thumbnail_directory: Path = asset_path.parent.parent / "thumbnails"
        thumbnail_path: Path = generate_thumbnail(asset_path, thumbnail_directory)
        asset: Asset = crud.asset.update(
            db, db_obj=asset, obj_in=AssetUpdate(thumbnail_path=str(thumbnail_path))
        )

        ##
        # Extract EXIF data
        ##
        exif_data: dict[str, Any] = extract_exif_data(asset_path)
        print(exif_data)
        exif_object: Exif = crud.exif.create(
            db, obj_in=ExifCreate(asset_id=asset_id, **exif_data)
        )

        ##
        # Conditionally geocode asset
        ##
        geocode_data: dict[str, str] = {}
        if all(
            (
                exif_object.latitude,
                exif_object.longitude,
                settings.GEOCODE_SERVICE != GeocodingService.none,
            )
        ):

            geocode_data: dict[str, str] = geocode(
                exif_object.latitude, exif_object.longitude, settings.GEOCODE_SERVICE
            )

        # we create a row even if we didn't geocode the photo
        # as this row is used for manual location-setting
        geocode_object: Geocode = crud.geocode.create(
            db, obj_in=GeocodeCreate(asset_id=asset_id, **geocode_data)
        )

        ##
        # Detect Objects
        ##

    return 1


# @huey.task()
# def check_if_duplicate():
#     ...


# @huey.task()
# def detect_objects():
#     ...


# # GEOCODE
