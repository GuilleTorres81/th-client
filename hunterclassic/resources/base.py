from hunterclassic.session import Session
from hunterclassic.models.user import User

class BaseResource:
    BASE_URL = "https://api.thehunter.com"

    def __init__(self, session: Session):
        self.session = session

    def post(self, endpoint: str, data: dict):
        response = self.session.post(
            f"{self.BASE_URL}{endpoint}",
            data=data,
        )

        response.raise_for_status()

        return response.json()
    
    @staticmethod
    def _user_id(user: User | int) -> int:
        return user.id if isinstance(user, User) else user