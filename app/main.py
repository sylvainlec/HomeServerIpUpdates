from ipGetter import IpGetter
from telegramNotifier import TelegramNotifier

ipGetter=IpGetter()
ipAddr=ipGetter.get()
logger=TelegramNotifier()
logger.Log(ipAddr)