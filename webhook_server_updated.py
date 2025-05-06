from flask import Flask, request, jsonify
import requests
import os
import json
from datetime import datetime
from waitress import serve

app = Flask(__name__)

# ✅ ROUTE VOOR TELEGRAM: /subscribe-commando
@app.route("/telegram-webhook", methods=["POST"])
def telegram_webhook():
    data = request.get_json()
    print("📨 Telegram webhook ontvangen:", data)

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
            subscribers[chat_id] = {
                "username": chat.get("username", ""),
                "subscribed_on": datetime.utcnow().isoformat()
            }

            with open(path, "w") as file:
                json.dump(subscribers, file, indent=2)

            reply = f"✅ Je bent ingeschreven voor SymbioBot alerts, @{chat.get('username', '')}!"
        else:
            reply = "ℹ️ Je was al geabonneerd."

        telegram_api = f"https://api.telegram.org/bot{os.environ.get('BOT_TOKEN')}/sendMessage"
        payload = {
            "chat_id": chat_id,
            "text": reply
        }
        requests.post(telegram_api, json=payload)

    return jsonify({"status": "ok"}), 200

# ✅ Start de server met waitress (vereist op Render)
from waitress import serve

if __name__ == '__main__':
    serve(app, host="0.0.0.0", port=10000)

