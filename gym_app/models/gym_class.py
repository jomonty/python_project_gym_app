from models.image_path import ImagePath

class GymClass:
    def __init__(self, name: str, active: bool, capacity: int, image_path: ImagePath, id: int = None):
        self.name = name
        self.active = active
        self.capacity = capacity
        self.image_path = image_path
        self.id = id