from models.member import Member
from models.gym_class import GymClass

class Booking:
    def __init__(self, member: Member, gym_class: GymClass):
        self.member = member
        self.gym_class = gym_class