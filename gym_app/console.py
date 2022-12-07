from random import choice
from datetime import date, time, timedelta

from models.member import Member
from models.gym_class import GymClass
from models.booking import Booking
from models.news import News
import repositories.member_repo as member_repo
import repositories.gym_class_repo as gym_class_repo
import repositories.booking_repo as booking_repo
import repositories.admin_repo as admin_repo
import repositories.news_repo as news_repo

booking_repo.delete_all()
member_repo.delete_all()
gym_class_repo.delete_all()
news_repo.delete_all()

members = []
for i in range(0,10):
    first_name = 'Member '
    last_name = str(i)
    is_premium = True if i%2==0 else False
    is_active = True if i < 9 else False
    member = Member(first_name, last_name, is_premium, is_active)
    member = member_repo.save(member)
    members.append(member)
    

gym_classes = []

con_start_date = date(2022, 12, 12)
for week in range(0,4):
    con_start_date = con_start_date + timedelta(days=(7 * week))
    for day in range(0,3):
        class_date = con_start_date + timedelta(days=(2 * day))
        class_time = time(6, 30, 0)
        gym_class = GymClass('Conditioning', class_date, class_time, 5, True)
        gym_class = gym_class_repo.save(gym_class)
        gym_classes.append(gym_class)
            
        
yog_start_date = date(2022, 12, 6)
for week in range(0,4):
    yog_start_date = yog_start_date + timedelta(days=(7 * week))
    for day in range(0,2):
        class_date = yog_start_date + timedelta(days=(2 * day))
        class_time = time(9, 0, 0)
        gym_class = GymClass('Yoga', class_date, class_time, 5, True)
        gym_class = gym_class_repo.save(gym_class)
        gym_classes.append(gym_class)
        
cro_start_date = date(2022, 12, 7)
for week in range(0,4):
    cro_start_date = cro_start_date + timedelta(days=(7 * week))
    for day in range(0,2):
        class_date = cro_start_date + timedelta(days=(2 * day))
        class_time = time(18, 0, 0)
        gym_class = GymClass('CrossFit', class_date, class_time, 5, True)
        gym_class = gym_class_repo.save(gym_class)
        gym_classes.append(gym_class)
        
aer_start_date = date(2022, 12, 5)
for week in range(0,4):
    aer_start_date = aer_start_date + timedelta(days=(7 * week))
    for day in range(0,2):
        class_date = aer_start_date + timedelta(days=(3 * day))
        class_time = time(19, 30, 0)
        gym_class = GymClass('Aerobics', class_date, class_time, 5, True)
        gym_class = gym_class_repo.save(gym_class)
        gym_classes.append(gym_class)
        
        
for i in range(0,3):
    gym_class = choice(gym_classes)
    gym_class.is_active = False
    gym_class_repo.update(gym_class)
    
gym_classes = gym_class_repo.select_all()

for member in members:
    for i in range(0,10):
        gym_class = choice(gym_classes)
        if not gym_class.is_active or not member.is_active:
            continue
        elif gym_class.class_date < date.today():
            continue
        elif gym_class.is_peak and not member.is_premium:
            continue
        elif admin_repo.is_class_full(gym_class):
            continue
        elif member in admin_repo.get_all_booked_members(gym_class.id):
            continue
        else:
            booking = Booking(gym_class, member)
            booking_repo.save(booking)
    

gym_classes = gym_class_repo.select_all_upcoming()

for i in range(0, 4):
    gym_class = gym_classes[i]
    while_count = 0
    while not admin_repo.is_class_full(gym_class):
        for member in admin_repo.select_all_members_for_booking(gym_class):
            if gym_class.is_peak and not member.is_premium:
                continue
            if not member.is_active:
                continue
            booking = Booking(gym_class, member)
            booking_repo.save(booking)
        while_count += 1
        if while_count == 10: break
    
    
news_1 = News('New website coming soon..')
news_repo.save_one(news_1)
news_2 = News('New website is live!')
news_repo.save_one(news_2)

# breakpoint()