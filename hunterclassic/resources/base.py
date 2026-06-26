from hunterclassic.session import Session


class BaseResource:
    def __init__(self, session: Session):
        self.session = session