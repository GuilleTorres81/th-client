from pydantic import BaseModel, ConfigDict


class HunterModel(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )