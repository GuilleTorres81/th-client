from .resources.users import UsersResource
from .resources.expeditions import ExpeditionsResource
from .session import Session


class HunterClient:

    def __init__(self):
        self.session = Session()

        self.users = UsersResource(self.session)
        self.expeditions = ExpeditionsResource(self.session)