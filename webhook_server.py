from flask import Flask, request, jsonify
from waitress import serve
import os
import json
from datetime import datetime

app = Flask(__name__)  # maak app aan

# ✅ Webhook endpoint
@app.route("/telegram-webhook", methods=["POST"])
def telegram_webhook():
    print("✅ Webhook HIT!")
    print("📩 Headers:", dict(request.headers))
    print("🧠 Body:", request.data.decode("utf-8"))
    return jsonify(success=True)

# ✅ Test endpoint
@app.route("/")
def home():
    return "✅ Webhook server draait!"

# ✅ Start de server met Waitress (vereist op Render)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    serve(app, host="0.0.0.0", port=port)
