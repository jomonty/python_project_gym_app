class Member:
    def __init__(self, first_name: str, last_name: str, age: int, address: str, id: int = None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.address = address
        self.id = id
        
    def get_full_name(self) -> str:
        return f'{self.first_name.title()} {self.last_name.title()}'