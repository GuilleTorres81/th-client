from .base import HunterModel
from pydantic import field_validator

class Skills(HunterModel):
    tracking: list[float]
    spotting: list[float]
    weapon: dict[int, float]

    @field_validator("weapon", mode="before")
    @classmethod
    def convert_keys(cls, value):
        return {int(k): v for k, v in value.items()}