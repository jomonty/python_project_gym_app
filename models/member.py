class Member:
    def __init__(self, first_name: str, last_name: str, is_premium: bool, is_active: bool, id: int = None):
        self.first_name = first_name
        self.last_name = last_name
        self.is_premium = is_premium
        self.is_active = is_active
        self.id = id
        
    def get_full_name(self):
        return f'{self.first_name.title()} {self.last_name.title()}'