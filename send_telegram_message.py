<<<<<<< HEAD
import os
import requests
from dotenv import load_dotenv

# 📂 Laad .env variabelen
load_dotenv()

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

# 🔧 Variabelen voor het testbericht
ticker = "GBP/JPY"
setup = "1H SMA hit"
price = "200.65"
time = "2025-05-05 15:00"
chart_url = "https://www.tradingview.com/chart/XaqcQlxu/"

# 🛠️ Opbouw van het bericht
message = (
    f"🔔 *Nieuw signaal ontvangen!*\n"
    f"*Pair:* {ticker}\n"
    f"*Setup:* {setup}\n"
    f"*Prijs:* {price}\n"
    f"*Tijd:* {time}\n"
    f"📈 [Bekijk chart]({chart_url})"
)

# 📬 Telegram API endpoint
url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

# 📦 Payload
payload = {
    'chat_id': CHAT_ID,
    'text': message,
    'parse_mode': 'Markdown'
}

# 🚀 Verstuur bericht
response = requests.post(url, json=payload)

# 🖨️ Feedback
print("Status:", response.status_code)
print("Response:", response.json())
=======
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
>>>>>>> 1071bfae841e2c799c8c7c251bbf60c8adfa0d4a
