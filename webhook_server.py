
from flask import Flask, request, jsonify
import requests
import json
import os
from datetime import datetime

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("📩 Webhook ontvangen:", data)

    # ✅ Nieuw: subscribe-functionaliteit
    message = data.get("message", {})
    text = message.get("text", "")
    chat = message.get("chat", {})
    chat_id = str(chat.get("id"))

    if text == "/subscribe" and chat_id:
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

        confirmation = f"✅ Je bent ingeschreven voor SymbioBot alerts, @{chat.get('username', '')}!"
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        payload = {
            'chat_id': chat_id,
            'text': confirmation
        }
        requests.post(url, json=payload)
        return jsonify({"status": "subscribed"}), 200

    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
