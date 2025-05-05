import os
import requests
from flask import Flask, request
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# ✅ Haal tokens uit Render environment variables
BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")
STUDENT_CHAT_ID = os.environ.get("STUDENT_CHAT_ID")  # optioneel

# ✅ Telegram API-endpoint
url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
print(f"BOT_TOKEN = '{BOT_TOKEN}'")

def send_telegram_message(text, chat_id=CHAT_ID):
    payload = {
        "chat_id": chat_id,
        "text": text
    }
    response = requests.post(url, json=payload)
    print("Telegram response:", response.status_code, response.text)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()

    ticker = data.get('ticker')
    setup = data.get('setup')
    price = data.get('price')
    time = data.get('time')
    chart_url = data.get('chart_url')

    # ✨ Bouw het bericht op
    message = (
        f"🔔 *Nieuw signaal ontvangen!*\n"
        f"*Pair:* {ticker}\n"
        f"*Setup:* {setup}\n"
        f"*Prijs:* {price}\n"
        f"*Tijd:* {time}\n"
        f"📈 [Bekijk chart]({chart_url})"
    )

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    payload_main = {
        'chat_id': CHAT_ID,
        'text': message,
        'parse_mode': 'Markdown'
    }

    response_main = requests.post(url, json=payload_main)
    print("Telegram hoofdgebruiker:", response_main.status_code, response_main.text)

    # Eventueel bericht naar student
    if STUDENT_CHAT_ID:
        payload_student = {
            'chat_id': STUDENT_CHAT_ID,
            'text': message,
            'parse_mode': 'Markdown'
        }
        response_student = requests.post(url, json=payload_student)
        print("Telegram student:", response_student.status_code, response_student.text)

    return {'status': 'ok'}, 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)





