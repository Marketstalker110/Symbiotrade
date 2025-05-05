import requests

BOT_TOKEN = "8165106767:AAHCi1ym60iBo-46c5dJZ3ZfE86EtHEBQSk"  # ← jouw token
url = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates"

response = requests.get(url)
print(response.json())

