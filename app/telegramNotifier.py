import requests
import os

class TelegramNotifier:
    def Log(self,message):
        token=os.getenv("TELEGRAM_BOT_TOKEN")
        chatId=os.getenv("TELEGRAM_CHAT_ID")
        url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chatId}&text={message}"
        requests.get(url).json()