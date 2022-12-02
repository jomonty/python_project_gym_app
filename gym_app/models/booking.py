from models.member import Member
from models.class_schedule import ClassSchedule

class Booking:
    def __init__(self, member: Member, class_schedule: ClassSchedule):
        self.member = member
        self.class_schedule = class_schedule