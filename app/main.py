from _version import __version__
from opyoid import Injector
from modules.module import AppModule
from ipApp import IpApp
print(f'Running HomeServerIpUpdates version {__version__}')
injector=Injector([AppModule])
app=injector.inject(IpApp)
app.run()