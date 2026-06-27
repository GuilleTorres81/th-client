from .base import HunterModel

from .expedition import Expedition


class ExpeditionList(HunterModel):
    total: int
    expeditions: list[Expedition]