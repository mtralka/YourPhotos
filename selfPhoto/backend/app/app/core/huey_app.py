from huey import PriorityRedisHuey

from .config import settings


huey = PriorityRedisHuey(
    settings.PROJECT_NAME, host=settings.REDIS_HOST, port=settings.REDIS_PORT
)
