from hunterclassic import HunterClient
from hunterclassic.models.user import User


def get_client() -> HunterClient:
    return HunterClient()


def iter_expeditions(client: HunterClient, user: User):
    history = client.expeditions.list(user)

    for expedition in history.expeditions:
        yield client.expeditions.get(user, expedition.id)