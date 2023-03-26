import time
from appConfig import AppConfig
from ipGetter import IpGetter
from telegramNotifier import TelegramNotifier

config=AppConfig()
ipGetter=IpGetter()
logger=TelegramNotifier(config)

lastIpAddress=ipGetter.get()
logger.Log(f'Service restarted, current IP address: {lastIpAddress}')

while True:
    time.sleep(config.SleepTime)
    newIpAddress=ipGetter.get()
    if lastIpAddress!=newIpAddress:
        logger.Log(f'New IP address detected: {newIpAddress}')
        lastIpAddress=newIpAddress