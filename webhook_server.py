
from flask import Flask, request, jsonify
import requests

# Telegram-gegevens
BOT_TOKEN = '8165106767:AAHC1iym60iBo-46c5dJZ3ZF8E6tHEBQS'  # <-- Jouw echte token
CHAT_ID = '6154157890'  # <-- Jouw bevestigde chat ID

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("✅ Webhook ontvangen:")
    print(data)

    # Bericht formatteren
    message = (
        f"🚨 *Nieuwe TradingView Alert!*\n\n"
        f"*Ticker:* {data.get('ticker', 'N/A')}\n"
        f"*Prijs:* {data.get('price', 'N/A')}\n"
        f"*Tijd:* {data.get('time', 'N/A')}\n"
        f"*Alert:* {data.get('alert_name', 'N/A')}"
    )

    # Telegram-verzending
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': CHAT_ID,
        'text': message,
        'parse_mode': 'Markdown'
    }

    response = requests.post(url, json=payload)

    # Debug output
    print("📤 Telegram-status:", response.status_code)
    print("📬 Telegram-antwoord:", response.json())

    return jsonify({"status": "bericht verzonden"}), 200

if __name__ == '__main__':
    app.run(port=5000)

from flask import Flask, request, jsonify
import requests

# Telegram-gegevens
BOT_TOKEN = '8165106767:AAHC1iym60iBo-46c5dJZ3ZF8E6tHEBQS'  # <-- Jouw echte token
CHAT_ID = '6154157890'  # <-- Jouw bevestigde chat ID

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("✅ Webhook ontvangen:")
    print(data)

    # Bericht formatteren
    message = (
        f"🚨 *Nieuwe TradingView Alert!*\n\n"
        f"*Ticker:* {data.get('ticker', 'N/A')}\n"
        f"*Prijs:* {data.get('price', 'N/A')}\n"
        f"*Tijd:* {data.get('time', 'N/A')}\n"
        f"*Alert:* {data.get('alert_name', 'N/A')}"
    )

    # Telegram-verzending
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': CHAT_ID,
        'text': message,
        'parse_mode': 'Markdown'
    }

    response = requests.post(url, json=payload)

    # Debug output
    print("📤 Telegram-status:", response.status_code)
    print("📬 Telegram-antwoord:", response.json())

    return jsonify({"status": "bericht verzonden"}), 200

if __name__ == '__main__':
    app.run(port=5000)

