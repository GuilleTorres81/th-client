from hunterclassic.models.user import User
from .base import BaseResource
from hunterclassic.models.skills import Skills

class UsersResource(BaseResource):

    def get_by_hostname(self, hostname: str):
        data = self.post(
            "/v1/Public_user/getByHostname",
            {
                "hostname": hostname,
            },
        )

        return User.model_validate(data)
    
    def get_achievements(self, user: User | int):
        user_id = self._user_id(user)

        return self.post(
            "/v1/Achievement/stats",
            {
                "user_id": user_id,
            },
        )

    def get_skills(self, user: User | int) -> Skills:
        user_id = self._user_id(user)

        data = self.post(
            "/v1/Skill/list",
            {
                "user_id": user_id,
            },
        )

        return Skills.model_validate(data)

    def get_statistics(self, user: User):
        user_id = self._user_id(user)

        data = self.post(
            "/v1/Statistics/total",
            {
                "user_id": user_id,
                "game_id": 12,
            },
        )

        return data

    def get_trophies(self, user: User):
        pass