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
