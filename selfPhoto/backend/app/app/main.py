from fastapi import FastAPI
from fastapi.routing import APIRoute
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware

from app.api.v1.api import api_router
from app.core.config import settings
from app.core.huey_app import huey
# from app.tasks.asset import check_if_duplicate
# from app.tasks.asset import detect_objects
from app.tasks.asset import extract_exif_data
from app.tasks.asset import generate_thumbnail
from app.tasks.asset import geocode
from app.tasks.asset import process_asset


def custom_generate_unique_id(route: APIRoute):
    return f"{route.tags[0].value}-{route.name}"


app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json",generate_unique_id_function=custom_generate_unique_id
)

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        # TODO change this back
        # allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_router, prefix=settings.API_V1_STR)
