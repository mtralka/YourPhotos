from fastapi import HTTPException


def raise_permissions_error() -> None:
    raise HTTPException(
        status_code=400, detail="The user doesn't have enough privileges"
    )


def raise_not_exists(name: str = "object") -> None:
    raise HTTPException(
        status_code=404,
        detail=f"This {name} does not exist",
    )
