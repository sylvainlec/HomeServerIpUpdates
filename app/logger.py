import requests

from appConfig import IConfig


class ILogger:
    def Log(self, message:str) -> None:
        pass

class TelegramNotifier(ILogger):
    def __init__(self,config:IConfig):
        self.botToken=config.BotToken
        self.chatId=config.ChatId

    def Log(self,message:str) -> None:
        url = f"https://api.telegram.org/bot{self.botToken}/sendMessage?chat_id={self.chatId}&text={message}"
        requests.get(url).json()

class LoggerDebug(ILogger):
    def Log(self,message:str) -> None:
        print(message)