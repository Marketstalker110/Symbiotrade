from flask import Flask, request
import requests

# === BOTGEGEVENS INVULLEN ===
BOT_TOKEN = '8165106767:AAHCi1ym60iBo-46c5dJZ3ZfE86EtHEBQSk'
CHAT_ID = '6154157890'

app = Flask(__name__)

# Mapping van setups naar uitleg
setup_uitleg = {
    "tp1": "Prijs keert terug naar ongeteste TP1-zone.",
    "tp1v": "TP1-extensiezone wordt getest na Fib-validatie.",
    "sub-cross": "SMA20 kruist over SMA80, mogelijke trendwijziging.",
    "eqb": "Equal Low doorbroken – mogelijke bullish reactie.",
    "eqh": "Equal High doorbroken – mogelijke bearish reactie."
}

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': CHAT_ID,
        'text': message
    }
    requests.post(url, json=payload)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json

    custom_alert = {
        "ticker": data.get("ticker", "Onbekend"),
        "price": data.get("price", "n.v.t."),
        "time": data.get("time", "n.v.t."),
        "setup": data.get("setup", "Geen setup"),
        "chart_url": data.get("chart_url", None)
    }

    uitleg = setup_uitleg.get(custom_alert["setup"], "Geen verdere uitleg.")

    # Opbouwen van het Telegram-bericht
    message_lines = [
        f"🚨 Symbio Alert: [{custom_alert['setup']}]",
        f"*Ticker:* {custom_alert['ticker']}",
        f"*Prijs:* {custom_alert['price']}",
        f"*Tijd:* {custom_alert['time']}",
        f"🧠 *Uitleg:* {uitleg}"
    ]

    # Voeg de grafieklink toe als die bestaat
    if custom_alert["chart_url"]:
        message_lines.append(f"📈 [Open grafiek in TradingView]({custom_alert['chart_url']})")

    telegram_message = "\n".join(message_lines)
    send_telegram_message(telegram_message)

    return "✅ Alert ontvangen en doorgestuurd", 200

if __name__ == '__main__':
    app.run(port=5000)