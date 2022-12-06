from random import choice
from datetime import date, time

from models.member import Member
from models.gym_class import GymClass
from models.booking import Booking
import repositories.member_repo as member_repo
import repositories.gym_class_repo as gym_class_repo
import repositories.booking_repo as booking_repo

booking_repo.delete_all()
member_repo.delete_all()
gym_class_repo.delete_all()

members = []
for i in range(0,10):
    first_name = 'Member '
    last_name = str(i)
    is_premium = True if i%2==0 else False
    is_active = True if i < 9 else False
    member = Member(first_name, last_name, is_premium, is_active)
    member = member_repo.save(member)
    members.append(member)
    
gym_class_1 = GymClass('Zumba', date(2022, 12, 5), time(7, 0, 0), 10, True)
gym_class_1 = gym_class_repo.save(gym_class_1)
gym_class_2 = GymClass('Conditioning', date(2022, 12, 7), time(6, 0, 0), 5, True)
gym_class_2 = gym_class_repo.save(gym_class_2)
gym_class_3 = GymClass('Yoga', date(2022, 12, 9), time(9, 0, 0), 8, True)
gym_class_3 = gym_class_repo.save(gym_class_3)
gym_class_4 = GymClass('CrossFit', date(2022, 12, 6), time(17, 0, 0), 4, False)
gym_class_4 = gym_class_repo.save(gym_class_4)
gym_class_5 = GymClass('Zumba', date(2022, 11, 5), time(20, 0, 0), 10, True)
gym_class_5 = gym_class_repo.save(gym_class_5)


gym_classes = [gym_class_1, gym_class_2, gym_class_3]

bookings = []
for member in members:
    gym_class = choice(gym_classes)
    booking = Booking(gym_class, member)
    booking_repo.save(booking)
    bookings.append(booking)

# breakpoint()