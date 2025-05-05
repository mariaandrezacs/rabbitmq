import requests

from variavel_ambiente import CHAT_ID, TOKEN

def send_telegram_message(message: str) -> None:
    token = TOKEN
    chat_id = CHAT_ID
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message
    }
    requests.post(url, data=payload)
