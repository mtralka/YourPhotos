from app.core.config import GeocodingService
from app.core.config import settings
from app.core.huey_app import huey
from geopy.geocoders import MapBox
from geopy.geocoders import Nominatim
from geopy.location import Location


# @huey.task()
def geocode(
    latitude: float, longitude: float, geocode_service: GeocodingService
) -> dict[str, str]:

    match geocode_service:
        case geocode_service.nominatim:
            geolocator = Nominatim(user_agent=settings.SERVER_NAME)
        case geocode_service.mapbox:
            geolocator = MapBox(
                api_key=settings.MAPBOX_API_KEY, user_agent=settings.SERVER_NAME
            )

    geolocation: Location = geolocator.reverse((latitude, longitude), exactly_one=True)

    results: dict[str, str] = {}
    target_attributes: tuple[str] = (
        "postcode",
        "place",
        "district",
        "region",
        "country",
    )

    if geolocation.address is None:
        return results

    results["address"] = geolocation.address

    match geocode_service:
        case geocode_service.nominatim:
            if (context := geolocation.raw.get("address")) is not None:
                results["postcode"] = context.get("postcode")
                results["country"] = context.get("country")
                results["region"] = context.get("state", context.get("city"))
                results["district"] = context.get("county")
                results["place"] = context.get("county")
        case geocode_service.mapbox:
            if (context := geolocation.raw.get("context")) is not None:
                for item in context:
                    results |= {
                        target: item.get("text")
                        for target in target_attributes
                        if target in item.get("id", [])
                    }

    return results
