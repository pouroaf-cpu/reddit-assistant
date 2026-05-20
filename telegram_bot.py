import requests
import os

def send_draft(message):
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    requests.post(url, data={
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "Markdown"
    })
