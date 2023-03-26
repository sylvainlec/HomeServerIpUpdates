from opyoid import Injector
from modules.module import AppModule
from ipApp import IpApp

injector=Injector([AppModule])
app=injector.inject(IpApp)
app.run()