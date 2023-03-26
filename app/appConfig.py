import os

class AppConfig:
    def __init__(self):
        self._sleepTime=int(os.getenv("SLEEP_TIME_BETWEEN_CHECKS"))
        self._botToken=os.getenv("TELEGRAM_BOT_TOKEN")
        self._chatId=os.getenv("TELEGRAM_CHAT_ID")

    @property
    def SleepTime(self):
        return self._sleepTime
    @property
    def BotToken(self):
        return self._botToken
    @property
    def ChatId(self):
        return self._chatId