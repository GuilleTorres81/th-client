from hunterclassic import HunterClient

client = HunterClient()

response = client.session.get("/v1/Application/discounts")

print(response.status_code)
print(response.headers["Content-Type"])
print(response.text[:500])