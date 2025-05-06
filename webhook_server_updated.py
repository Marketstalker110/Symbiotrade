from flask import Flask, request, jsonify
import requests
import json
from datetime import datetime

app = Flask(__name__)

# 🔔 ROUTE VOOR TELEGRAM: /subscribe-commando
@app.route("/telegram-webhook", methods=["POST"])
def telegram_webhook():
    data = request.get_json()
    print("📩 Telegram webhook ontvangen:", data)

    message = data.get("message", {})
    text = message.get("text", "").strip()
    chat = message.get("chat", {})
    chat_id = str(chat.get("id"))

    if text.lower() == "/subscribe" and chat_id:
        path = "subscribers.json"

        try:
            with open(path, "r") as file:
                subscribers = json.load(file)
        except FileNotFoundError:
            subscribers = {}

        if chat_id not in subscribers:
            # Nieuw lid toevoegen
            subscribers[chat_id] = {
                "username": chat.get("username", ""),
                "subscribed_on": datetime.utcnow().isoformat()
            }

            with open(path, "w") as file:
                json.dump(subscribers, file, indent=2)

            reply = f"✅ Je bent ingeschreven voor Symbiobot alerts, @{chat.get('username', '')}!"
        else:
            reply = "ℹ️ Je was al geabonneerd."

        # Stuur reply terug via Telegram
        TG_API = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        payload = {
            "chat_id": chat_id,
            "text": reply
        }
        requests.post(TG_API, json=payload)

    return jsonify({"status": "ok"}), 200


# ✅ WEBHOOK TEST ENDPOINT
@app.route("/webhook", methods=["POST"])
def test_webhook():
    data = request.json
    print("🧪 Webhook ontvangen:", data)
    return jsonify({"status": "success"}), 200


if __name__ == "__main__":
    app.run(port=5000)
