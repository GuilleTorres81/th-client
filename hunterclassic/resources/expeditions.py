from hunterclassic.models.user import User
from hunterclassic.models.expedition_list import ExpeditionList
from .base import BaseResource


class ExpeditionsResource(BaseResource):

    def list(self, user: User | int, offset: int = 0, limit: int = 40,):
        user_id = self._user_id(user)

        data = self.post(
            "/v1/Expedition/list",
            {
                "user_id": user_id,
                "offset": offset,
                "limit": limit,
            },
        )

        return ExpeditionList.model_validate(data)
        
    def get(self, user: User | int, expedition_id: int):
        user_id = self._user_id(user)

        return self.post(
            "/v1/Public_user/expedition",
            {
                "user_id": user_id,
                "expedition_id": expedition_id,
            },
        )