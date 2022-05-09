from pathlib import Path
import re
from typing import Any
from typing import AnyStr
from typing import Pattern

from PIL import ExifTags
from PIL import Image
from app.core.huey_app import huey


split_on_uppercase: Pattern[AnyStr] = re.compile("[A-Z][^A-Z]*")


# @huey.task()
def extract_exif_data(file_path: Path) -> dict:
    def dms_to_decimal_degrees(
        dms: tuple[float, float, float], direction: str
    ) -> float:
        degrees, minutes, seconds = dms
        compass_direction: int = -1 if direction in ("W", "S") else 1

        return (degrees + (minutes / 60) + (seconds / 3600)) * compass_direction

    asset = Image.open(file_path)

    if (raw_exif := asset._getexif()) is None:
        return {}

    raw_exif_data: dict[str, Any] = {
        ExifTags.TAGS[k]: v for k, v in raw_exif.items() if k in ExifTags.TAGS
    }

    if (gps_exif := raw_exif_data.get("GPSInfo")) is not None:

        raw_gps_data: dict[str, Any] = {
            ExifTags.GPSTAGS[k]: gps_exif[k]
            for k in gps_exif.keys()
            if k in ExifTags.GPSTAGS
        }

        for key in ("latitude", "longitude"):
            value = raw_gps_data.get(f"GPS{key.capitalize()}")
            ref = raw_gps_data.get(f"GPS{key.capitalize()}Ref")

            if not all((value, ref)):
                break

            raw_exif_data[key] = dms_to_decimal_degrees(value, ref)

        if altitude := raw_gps_data.get("GPSAltitude"):
            raw_exif_data["altitude"] = altitude

        raw_exif_data.pop("GPSInfo", None)

    exif_data: dict[str, Any] = {
        "_".join(re.findall(split_on_uppercase, k.capitalize())).lower(): v
        for k, v in raw_exif_data.items()
    }

    return exif_data
