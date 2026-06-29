from pprint import pprint

from hunterclassic import HunterClient

client = HunterClient()

player = client.users.get_by_hostname("HunterLagger")

history = client.expeditions.list(player)

expedition = history.expeditions[0]

detail = client.expeditions.get(
    player,
    expedition.id,
)

pprint(detail)