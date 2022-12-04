class GymClass:
    def __init__(self, name: str, class_date: str, class_time: str, capacity: int, is_active: bool, id: int = None):
        self.name = name
        self.class_date = class_date
        self.class_time = class_time
        self.capacity = capacity
        self.is_active = is_active
        self.id = id