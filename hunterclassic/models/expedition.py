from .base import HunterModel


class Expedition(HunterModel):
    id: int
    reserve: int
    location_id: int | None = None
    kills: int
    collectables: int
    singleplayer: bool
    start_ts: int
    end_ts: int
    map: int