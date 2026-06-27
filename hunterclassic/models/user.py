from pydantic import BaseModel


class User(BaseModel):
    id: int
    hostname: str
    handle: str
    avatar: str | None = None
    online: bool
    hunterscore: int