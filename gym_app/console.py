from random import choice as ran_choice

from models.plan import Plan
from models.member import Member
from models.subscription import Subscription
from models.class_type import ClassType
from models.instructor import Instructor
from models.gym_class import GymClass
from models.booking import Booking

plan_1 = Plan('Standard', False)
plan_2 = Plan('Premium', True)
plan_3 = Plan('Student', True)
plans = [plan_1, plan_2, plan_3]

members = []
for i in range(0, 10):
    member = Member('gym', f'member {i}', i + 20, f'Address {i}')
    members.append(member)

subscriptions = []
for member in members:
    sub = Subscription(member, ran_choice(plans), True)
    subscriptions.append(sub)
subscriptions[-1].active = False

instructor_1 = Instructor('Barry', 'Biceps')
instructor_2 = Instructor('Lisa', 'Legpress')
instructor_3 = Instructor('Stuart', 'Squats')

class_type_1 = ClassType('Cross Fit', True, 5)
class_type_2 = ClassType('Zumba', True, 6)
class_type_3 = ClassType('Conditioning', True, 4)
class_type_4 = ClassType('Cycling', True, 10)
class_type_5 = ClassType('Pilates', False, 8)


gym_class_1 = GymClass(class_type_1, instructor_1, '2022-12-01', '07:00', 60)
gym_class_2 = GymClass(class_type_1, instructor_1, '2022-12-08', '07:00', 60)
gym_class_3 = GymClass(class_type_1, instructor_1, '2022-12-15', '07:00', 60)
gym_class_4 = GymClass(class_type_2, instructor_2, '2022-12-01', '08:00', 45)
gym_class_5 = GymClass(class_type_2, instructor_2, '2022-12-08', '08:00', 45)
gym_class_6 = GymClass(class_type_2, instructor_2, '2022-12-15', '08:00', 45)
gym_class_7 = GymClass(class_type_3, instructor_3, '2022-12-01', '09:00', 30)
gym_class_8 = GymClass(class_type_3, instructor_3, '2022-12-08', '09:00', 30)
gym_class_9 = GymClass(class_type_3, instructor_3, '2022-12-15', '09:00', 30)
gym_class_10 = GymClass(class_type_4, instructor_1, '2022-12-01', '18:00', 60)
gym_class_11 = GymClass(class_type_4, instructor_1, '2022-12-08', '18:00', 60)
gym_class_12 = GymClass(class_type_4, instructor_1, '2022-12-15', '18:00', 60)
gym_class_13 = GymClass(class_type_5, instructor_2, '2022-12-01', '19:00', 30)
gym_class_14 = GymClass(class_type_5, instructor_2, '2022-12-08', '19:00', 30)
gym_class_15 = GymClass(class_type_5, instructor_2, '2022-12-15', '19:00', 30)

booking_1 = Booking(member_1, gym_class_1)
booking_2 = Booking(member_2, gym_class_1)
booking_3 = Booking(member_3, gym_class_1)

booking_4 = Booking(member_4, gym_class_4)
booking_5 = Booking(member_5, gym_class_4)
booking_6 = Booking(member_6, gym_class_4)
booking_7 = Booking(member_7, gym_class_4)

booking_8 = Booking(member_1, gym_class_7)
booking_9 = Booking(member_1, gym_class_7)
booking_10 = Booking(member_1, gym_class_7)
booking_11 = Booking(member_1, gym_class_7)

booking_13 = Booking(member_1, gym_class_10)
booking_14 = Booking(member_1, gym_class_10)
booking_15 = Booking(member_1, gym_class_10)
booking_16 = Booking(member_1, gym_class_10)
booking_17 = Booking(member_1, gym_class_10)
booking_18 = Booking(member_1, gym_class_10)

