from hunterclassic import HunterClient

client = HunterClient()

player = client.users.get_by_hostname("HunterLagger")

print(type(player))
print(player.keys())