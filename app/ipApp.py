import time

from appConfig import IConfig
from ipGetter import IIpGetter
from logger import ILogger

class IpApp:
    def __init__(self,
                 config:IConfig,
                 ipGetter:IIpGetter,
                 logger:ILogger) -> None:
        self.config=config
        self.ipGetter=ipGetter
        self.logger=logger

    def run(self) -> None:
        self.lastIpAddress=self.ipGetter.get()
        self.logger.Log(f'Service restarted, current IP address: {self.lastIpAddress}')

        while True:
            time.sleep(self.config.SleepTime)
            newIpAddress=self.ipGetter.get()
            if newIpAddress!=self.lastIpAddress:
                self.logger.Log(f'New IP address detected: {newIpAddress}')
                self.lastIpAddress=newIpAddress