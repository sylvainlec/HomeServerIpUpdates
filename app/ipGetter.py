import requests
import json

class IpGetter:
    endpoint = 'https://ipinfo.io/json'

    def get(self):

        response = requests.get(self.endpoint, verify = True)

        if response.status_code != 200:
            return 'Status:', response.status_code, 'Problem with the request. Exiting.'

        data = response.json()
        return data['ip']