from .session import Session
from .resources.users import UsersResource

class HunterClient:

    def __init__(self):
        self.session = Session()

        self.users = UsersResource(self.session)