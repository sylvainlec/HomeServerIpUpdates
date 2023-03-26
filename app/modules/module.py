from opyoid import Module

from ipApp import IpApp
from appConfig import IConfig,DebugConfig
from ipGetter import IpGetterDebug,IIpGetter
from logger import LoggerDebug,ILogger

class AppModule(Module):
    def configure(self) -> None:
        self.bind(IConfig,to_class=DebugConfig)
        self.bind(IIpGetter,to_class=IpGetterDebug)
        self.bind(ILogger,to_class=LoggerDebug)
        self.bind(IpApp)