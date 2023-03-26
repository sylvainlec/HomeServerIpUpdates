import random
import requests
import json

class IIpGetter:
    def get(self) -> str:
        pass
    
class IpGetterIpInfoRequest(IIpGetter):
    endpoint = 'https://ipinfo.io/json'
    def get(self) -> str:
        response = requests.get(self.endpoint, verify = True)

        if response.status_code != 200:
            return 'Status:', response.status_code, 'Problem with the request. Exiting.'

        data = response.json()
        return data['ip']

class IpGetterDebug(IIpGetter):
    def get(self) -> str:
        a=random.randrange(101, 255)
        b=random.randrange(101, 255)
        c=random.randrange(101, 255)
        d=random.randrange(101, 255)
        return f'{a}.{b}.{c}.{d}'