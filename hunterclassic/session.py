import requests


class Session:
    BASE_URL = "https://api.thehunter.com"

    def __init__(self):
        self._session = requests.Session()

    def get(self, endpoint: str, **kwargs):
        response = self._session.get(
            f"{self.BASE_URL}{endpoint}",
            **kwargs,
        )

        response.raise_for_status()
        return response

    def post(self, endpoint: str, **kwargs):
        response = self._session.post(
            f"{self.BASE_URL}{endpoint}",
            **kwargs,
        )

        response.raise_for_status()
        return response