from flask import Flask, request, jsonify
from waitress import serve
import os
import json
from datetime import datetime

app = Flask(__name__)  # maak app aan

# ✅ Webhook endpoint
@app.route("/telegram-webhook", methods=["POST"])
def telegram_webhook():
    data = request.get_json()
    print("📥 Webhook ontvangen:", data)

    message_text = data.get("message", {}).get("text", "")
    chat_id = data.get("message", {}).get("chat", {}).get("id")

    if message_text.lower() == "/subscribe":
        # Voeg chat_id toe aan subscribers.json
        try:
            with open("subscribers.json", "r") as f:
                subscribers = json.load(f)
        except FileNotFoundError:
            subscribers = []

        if chat_id not in subscribers:
            subscribers.append(chat_id)
            with open("subscribers.json", "w") as f:
                json.dump(subscribers, f, indent=2)
            reply = "✅ Je bent ingeschreven voor SymbioBot alerts!"
        else:
            reply = "ℹ️ Je was al geabonneerd."

        telegram_api = f"https://api.telegram.org/bot{os.environ.get('BOT_TOKEN')}/sendMessage"
        payload = {
            "chat_id": chat_id,
            "text": reply
        }
        requests.post(telegram_api, json=payload)

    return jsonify(success=True)


# ✅ Test endpoint
@app.route("/")
def home():
    return "✅ Webhook server draait!"

# ✅ Start de server met Waitress (vereist op Render)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    serve(app, host="0.0.0.0", port=port)
