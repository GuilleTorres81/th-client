from hunterclassic.models.user import User
from .base import BaseResource


class ExpeditionsResource(BaseResource):

    def list(self, user: User | int, offset: int = 0, limit: int = 40,):
        user_id = user.id if isinstance(user, User) else user

        return self.post(
            "/v1/Expedition/list",
            {
                "user_id": user_id,
                "offset": offset,
                "limit": limit,
            },
        )
        
    def get(self, user: User | int, expedition_id: int):
        user_id = user.id if isinstance(user, User) else user

        return self.post(
            "/v1/Public_user/expedition",
            {
                "user_id": user_id,
                "expedition_id": expedition_id,
            },
        )