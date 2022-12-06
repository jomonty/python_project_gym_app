from datetime import date, time

class GymClass:
    def __init__(self, name: str, class_date: date, class_time: time, capacity: int, is_active: bool, id: int = None):
        self.name = name
        self.class_date = class_date
        self.class_time = class_time
        self.capacity = capacity
        self.is_active = is_active
        self.is_peak = self.set_is_peak()
        self.id = id
        
    def set_is_peak(self):
        if self.class_time >= time(6,0,0) and self.class_time <= time(8,30,0):
            return True
        elif self.class_time >= time(17,0,0) and self.class_time <= time(19,0,0):
            return True
        else:
            return False

