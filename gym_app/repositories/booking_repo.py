from db.run_sql import run_sql
from models.booking import Booking
from models.member import Member
from models.gym_class import GymClass
import repositories.member_repo as member_repo
import repositories.gym_class_repo as gym_class_repo

# RESULT PARSER
def result_parser(results):
    bookings = []
    if results == None or len(results) == 0:
        return bookings
    else:
        for row in results:
            id = row['id']
            member = member_repo.select(row['member_id'])
            gym_class = gym_class_repo.select(row['class_id'])
            create_date = row['create_date']
            booking = Booking(gym_class, member, create_date, id)
            bookings.append(booking)
        return bookings

# SELECT ONE
def select(id: int) -> Booking:
    sql = """
            SELECT *
            FROM bookings
            WHERE id = %s
            """
    values = [id]
    results = run_sql(sql, values)
    bookings = result_parser(results)
    if len(bookings) >= 1:
        return bookings[0]

# SELECT ALL
def select_all() -> list[Booking]:
    sql = """
            SELECT *
            FROM bookings
            """
    results = run_sql(sql)
    return result_parser(results)

# SAVE ONE
def save(booking: Booking) -> Booking:
    sql = """
            INSERT INTO bookings 
            (class_id, member_id)
            VALUES
            (%s, %s)
            RETURNING *
            """
    values = [booking.gym_class.id, booking.member.id]
    results = run_sql(sql, values)
    bookings = result_parser(results)
    if len(bookings) >= 1:
        booking = bookings[0]
    return booking

# DELETE ONE
def delete(id: int) -> None:
    sql = """
            DELETE
            FROM bookings
            WHERE id = %s
            """
    values = [id]
    run_sql(sql, values)

# DELETE ALL
def delete_all() -> None:
    sql = """
            DELETE
            FROM bookings
            """
    run_sql(sql)

# UPDATE ONE
def update(booking: Booking) -> None:
    sql = """
            UPDATE bookings
            SET (class_id, member_id, update_date) = (%s, %s, %s)
            WHERE id = %s
            """
    values = [booking.gym_class.id, booking.member.id]
    run_sql(sql, values)