import os

class IConfig:
    @property
    def SleepTime(self):
        pass
    @property
    def BotToken(self):
        pass
    @property
    def ChatId(self):
        pass

class EnvFileConfig(IConfig):
    def __init__(self):
        self._sleepTime:int=int(os.getenv("SLEEP_TIME_BETWEEN_CHECKS"))
        self._botToken:str=os.getenv("TELEGRAM_BOT_TOKEN")
        self._chatId:str=os.getenv("TELEGRAM_CHAT_ID")

    @property
    def SleepTime(self):
        return self._sleepTime
    @property
    def BotToken(self):
        return self._botToken
    @property
    def ChatId(self):
        return self._chatId
    
class DebugConfig(IConfig):
    def __init__(self):
        self._sleepTime:int=2

    @property
    def SleepTime(self):
        return self._sleepTime