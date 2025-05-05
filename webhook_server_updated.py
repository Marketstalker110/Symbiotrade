from flask import Flask, request, jsonify
import requests
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

app = Flask(__name__)

def send_photo_to_telegram(photo_url, caption=""):
    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
    payload = {
        'chat_id': CHAT_ID,
        'photo': photo_url,
        'caption': caption
    }
    response = requests.post(telegram_url, data=payload)
    print("Telegram response (photo):", response.text)
    return response

def send_text_to_telegram(text):
    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': CHAT_ID,
        'text': text
    }
    response = requests.post(telegram_url, data=payload)
    print("Telegram response (text):", response.text)
    return response

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()

    ticker = data.get("ticker", "Onbekend")
    price = data.get("price", "N.v.t.")
    time = data.get("time", "N.v.t.")
    note = data.get("note", "📈 Nieuw signaal ontvangen!")
    chart = data.get("chart", "")

    # Bouw de caption op
    caption = f"{note}\n📊 Pair: {ticker}\n💰 Prijs: {price}\n🕒 Tijd: {time}"

    if chart.endswith(".png"):
        # Verstuur als afbeelding
        send_photo_to_telegram(chart, caption)
    else:
        # Verstuur als tekstbericht + link
        full_text = f"{caption}\n🔗 Chart: {chart}" if chart else caption
        send_text_to_telegram(full_text)

    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    app.run()





