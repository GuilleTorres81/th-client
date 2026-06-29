from hunterclassic.models.base import HunterModel

class Achievement(HunterModel):
    id: int
    category_id: int
    group_id: int
    value: int
    triggers: dict[str, int]