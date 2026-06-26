import requests


class Session:
    BASE_URL = "https://api.thehunter.com"

    def __init__(self):
        self._session = requests.Session()

    def get(self, url: str, **kwargs):
        return self._session.get(url, **kwargs)

    def post(self, url: str, **kwargs):
        return self._session.post(url, **kwargs)