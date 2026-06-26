from .base import BaseResource


class UsersResource(BaseResource):
    BASE_URL = "https://api.thehunter.com"

    def get_by_hostname(self, hostname: str):
        response = self.session.post(
            f"{self.BASE_URL}/v1/Public_user/getByHostname",
            data={
                "hostname": hostname,
            },
        )

        response.raise_for_status()

        return response.json()