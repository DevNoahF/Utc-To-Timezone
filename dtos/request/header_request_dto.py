from enum import Enum

from pydantic import BaseModel


class TypeTimezone(str, Enum):
    BRASIL = "America/Sao_Paulo"
    ESTADOS_UNIDOS = "America/New_York"


class Header(BaseModel):
    timezone: TypeTimezone