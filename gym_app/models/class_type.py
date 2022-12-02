from models.image_path import ImagePath

class ClassType:
    def __init__(self, name: str, active: bool, capacity: int, image_path: ImagePath = None, id: int = None):
        self.name = name
        self.active = active
        self.capacity = capacity
        self.image_path = image_path
        self.id = id