from db.run_sql import run_sql

from models.booking import Booking
from models.member import Member
from models.gym_class import GymClass

import repositories.member_repo as member_repo
import repositories.gym_class_repo as gym_class_repo
import repositories.booking_repo as booking_repo



# Return all gym_classes that a member is booked on
def get_all_booked_classes(id: int) -> list[GymClass]:
    sql = """
            SELECT c.*
            FROM bookings b
            INNER JOIN classes c on b.class_id = c.id
            WHERE b.member_id = %s
            ORDER BY c.class_date ASC, c.class_time ASC
            """
    values = [id]
    results = run_sql(sql, values)
    gym_classes = gym_class_repo.results_parser(results)
    return gym_classes

# SELECT ALL MEMBERS BOOKED ON A GYM CLASS
def get_all_booked_members(id: int) -> list[Member]:
    sql = """
            SELECT m.*
            FROM bookings b
            INNER JOIN members m
            ON b.member_id = m.id
            WHERE b.class_id = %s
            ORDER BY m.last_name ASC, m.first_name ASC
            """
    values = [id]
    results = run_sql(sql, values)
    members = member_repo.results_parser(results)
    return members

# IS CLASS FULL
def is_class_full(gym_class: GymClass) -> bool:
    sql = """
            SELECT count(*) count_booked
            FROM bookings b
            WHERE b.class_id = %s
            """
    values = [gym_class.id]
    results = run_sql(sql, values)
    if results:
        count_booked = results[0]['count_booked']
        if count_booked < gym_class.capacity:
            return False
    return True

# SELECT ALL ACTIVE MEMBERS NOT BOOKED ON CLASS
def select_all_members_for_booking(gym_class: GymClass) -> list[Member]:
    sql = """
            SELECT m.*
            FROM members m
            LEFT JOIN
            (SELECT * FROM bookings WHERE class_id = %s) b
            ON m.id = b.member_id
            WHERE b.id is null
            ORDER BY m.last_name ASC, m.first_name ASC
            """
    values = [gym_class.id]
    results = run_sql(sql, values)
    members = member_repo.results_parser(results)
    return members

# SELECT ALL ACTIVE, PREMIUM MEMBERS NOT BOOKED ON CLASS
def select_premium_members_for_booking(gym_class: GymClass) -> list[Member]:
    sql = """
            SELECT m.*
            FROM members m
            LEFT JOIN 
            (SELECT * FROM bookings WHERE class_id = %s) b
            ON m.id = b.member_id
            WHERE m.is_premium = true AND b.id is null
            ORDER BY m.last_name ASC, m.first_name ASC
            """
    values = [gym_class.id]
    results = run_sql(sql, values)
    members = member_repo.results_parser(results)
    return members
    
# SELECT ALL BOOKINGS FOR CLASS
def select_all_by_class(gym_class: GymClass) -> list[Booking]:
    sql = """
            SELECT *
            FROM bookings b
            LEFT JOIN members m on b.member_id = m.id
            WHERE class_id = %s
            ORDER BY m.last_name ASC, m.first_name ASC
            """
    values = [gym_class.id]
    results = run_sql(sql, values)
    bookings = booking_repo.result_parser(results)
    return bookings