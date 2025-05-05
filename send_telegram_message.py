import requests

# Jouw eigen gegevens
BOT_TOKEN = 'YOUR_BOT_TOK8165106767:AAHCi1ym60iBo-46c5dJZ3ZfE86EtHEBQSk'  # <-- Vervang dit door je echte token
CHAT_ID = '6154157890'

# Bericht dat je wilt versturen
message = "🚀 Hallo Eric! Dit is je eerste bericht vanuit jouw eigen SymbioBot."

# Telegram API-endpoint
url = f"https://api.telegram.org/bot8165106767:AAHCi1ym60iBo-46c5dJZ3ZfE86EtHEBQSk/sendMessage"

# Data payload
url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
payload = {
    'chat_id': CHAT_ID,
    'text': message
}

# POST-verzoek sturen
response = requests.post(url, json=payload)

# Feedback in de terminal
print("Status code:", response.status_code)
print("Antwoord:", response.json())
