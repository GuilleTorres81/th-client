from hunterclassic import HunterClient

client = HunterClient()

player = client.users.get_by_hostname("HunterLagger")

history = client.expeditions.list(player)

print(type(history))
print(type(history.expeditions[0]))

print(history.total)
print(history.expeditions[0].id)
print(history.expeditions[0].kills)
print(history.expeditions[0].singleplayer)