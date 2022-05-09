from humps import camelize
from pydantic import BaseModel


def to_camel(input: str) -> str:
    return camelize(input)


class CamelModel(BaseModel):
    class Config:
        alias_generator = to_camel
        allow_population_by_field_name = True
