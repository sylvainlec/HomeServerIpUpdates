from opyoid import Module

from ipApp import IpApp
from appConfig import IConfig,EnvFileConfig
from ipGetter import IIpGetter,IpGetterIpInfoRequest
from logger import ILogger, TelegramNotifier

class AppModule(Module):
    def configure(self) -> None:
        self.bind(IConfig,to_class=EnvFileConfig)
        self.bind(IIpGetter,to_class=IpGetterIpInfoRequest)
        self.bind(ILogger,to_class=TelegramNotifier)
        self.bind(IpApp)