import requests

from appConfig import AppConfig

class TelegramNotifier:
    def __init__(self,config:AppConfig):
        self.botToken=config.BotToken
        self.chatId=config.ChatId

    def Log(self,message) -> None:
        url = f"https://api.telegram.org/bot{self.botToken}/sendMessage?chat_id={self.chatId}&text={message}"
        requests.get(url).json()