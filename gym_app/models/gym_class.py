from models.class_type import ClassType
from models.instructor import Instructor

class GymClass:
    def __init__(self, class_type: ClassType, instructor: Instructor, date: str, start_time: str, duration_mins: int, id: int = None):
        self.class_type = class_type
        self.instructor = instructor
        self.date = date
        self.start_time = start_time
        self.duration_mins = duration_mins
        self.id = id