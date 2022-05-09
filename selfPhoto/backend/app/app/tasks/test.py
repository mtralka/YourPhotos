from typing import Generator

from app import crud
from app.core.huey_app import huey
from app.db.session import SessionLocal


# from sqlalchemy.orm import scoped_session


# Session = scoped_session(SessionLocal)


# @huey.on_startup()
# def open_db_connection():
#     db = SessionLocal()
#     if not db.is_closed():
#         db.close()
#     db.connect()


@huey.task()
def add_numbers(a, b):

    with SessionLocal() as db:
        asset = crud.asset.get_by_id(db, id=5)

        if not asset:
            print("NO ASASET")
        else:
            print(asset)

    return asset
