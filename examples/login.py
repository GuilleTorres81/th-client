from hunterclassic import HunterClient

client = HunterClient()

player = client.users.get_by_hostname("HunterLagger")

history = client.expeditions.list(player)

first = history["expeditions"][0]

hunt = client.expeditions.get(
    player,
    first["id"],
)

print(hunt)