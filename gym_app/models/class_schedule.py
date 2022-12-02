from models.gym_class import GymClass
from models.instructor import Instructor

class ClassSchedule:
    def __init__(self, gym_class: GymClass, instructor: Instructor, date: str, start_time: str, duration_mins: int, id: int = None):
        self.gym_class = gym_class
        self.instructor = instructor
        self.date = date
        self.start_time = start_time
        self.duration_mins = duration_mins
        self.id = id