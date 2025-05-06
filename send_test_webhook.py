import requests

url = "https://symbiotradebot.onrender.com/webhook"  # <-- jouw Flask endpoint bij Render

payload = {
    "ticker": "GBP/JPY",
    "price": "198.500",
    "setup": "TP1 zone raak",
    "time": "2025-05-05 21:10",
    "note": "test direct webhook",
    "chart": "https://www.tradingview.com/x/XacQUEKO/"
}

response = requests.post(url, json=payload)
print("Status:", response.status_code)
print("Response:", response.text)




