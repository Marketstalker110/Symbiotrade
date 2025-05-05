import os
import requests
from dotenv import load_dotenv

# Laad variabelen uit .env
load_dotenv()

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

message = "✅ Lukt het?"

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
payload = {
    'chat_id': CHAT_ID,
    'text': message
}

response = requests.post(url, json=payload)
print("Status:", response.status_code)
print("Response:", response.json())


