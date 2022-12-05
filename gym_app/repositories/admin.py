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
            """
    values = [id]
    results = run_sql(sql, values)
    gym_classes = gym_class_repo.results_parser(results)
    return gym_classes