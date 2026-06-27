from hunterclassic.models.user import User
from .base import BaseResource


class UsersResource(BaseResource):

    def get_by_hostname(self, hostname: str):
        data = self.post(
            "/v1/Public_user/getByHostname",
            {
                "hostname": hostname,
            },
        )

        return User.model_validate(data)