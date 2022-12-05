from datetime import datetime
from models.gym_class import GymClass
from models.member import Member

class Booking:
    def __init__(self,
                 gym_class: GymClass, 
                 member: Member, 
                 create_date: datetime = None, 
                 id: int = None):
        self.gym_class = gym_class
        self.member = member
        self.create_date = create_date
        self.id = id
