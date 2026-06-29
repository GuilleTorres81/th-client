from hunterclassic.models.base import HunterModel
from hunterclassic.models.achievement import Achievement

class Achievements(HunterModel):
    items: list[Achievement]

    @classmethod
    def from_api(cls, data: list[dict]):
        return cls(
            items=[Achievement.model_validate(item) for item in data]
        )

    def __iter__(self):
        return iter(self.items)

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]