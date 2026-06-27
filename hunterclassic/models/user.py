from .base import HunterModel


class User(HunterModel):
    id: int
    hostname: str
    handle: str
    avatar: str | None = None
    online: bool
    hunterscore: int