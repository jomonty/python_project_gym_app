class Plan:
    def __init__(self, type: str, is_premium: bool, id: int = None):
        self.id = id
        self.type = type
        self.is_premium = is_premium