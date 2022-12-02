from models.plan import Plan
from models.member import Member

class Subscription:
    def __init__(self, member: Member, plan: Plan, active: bool, id: int = None):
        self.member = member
        self.plan = plan
        self.active = active
        self.id = id
        
    def is_active(self) -> bool:
        return self.active
    
    def is_premium(self) -> bool:
        return self.plan.is_premium