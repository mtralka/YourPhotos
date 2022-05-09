from pathlib import Path

from PIL import Image
from app.core.config import settings
from app.core.huey_app import huey


# @huey.task()
def generate_thumbnail(asset_path: Path, thumbnail_directory: Path) -> Path:
    """
    Steps

    1. Retrieve asset

    """
    thumbnail_path: Path = thumbnail_directory / f"{asset_path.stem}.thumbnail.webp"

    # get asset
    with Image.open(asset_path) as im:
        im.thumbnail(settings.THUMBNAIL_SIZE)
        im.save(thumbnail_path, "WEBP")

    return thumbnail_path
