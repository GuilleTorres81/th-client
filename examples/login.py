from pprint import pprint

from hunterclassic import HunterClient

client = HunterClient()

player = client.users.get_by_hostname("HunterLagger")

skills = client.users.get_skills(player)

print(type(skills))
pprint(skills)