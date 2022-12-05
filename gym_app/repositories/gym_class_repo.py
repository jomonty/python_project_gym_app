from datetime import date, time
from db.run_sql import run_sql
from models.gym_class import GymClass
from models.member import Member

# SELECT ONE
def select(id: int) -> GymClass:
    sql = """
            SELECT *
            FROM classes
            WHERE id = %s
            """
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        name = result['name']
        class_date = date.fromisoformat(result['class_date'])
        class_time = time.fromisoformat(result['class_time'])
        capacity = result['capacity']
        is_active = result['is_active']
        id = result['id']
        gym_class = GymClass(name, class_date, class_time, capacity, is_active, id)
        return gym_class

# SELECT ALL
def select_all(upcoming=False, inactive=False, historical=False) -> list[GymClass]:
    if upcoming == True:
        sql = """SELECT * FROM classes WHERE date >= CURRENT_DATE"""
    elif inactive == True:
        sql = """SELECT * FROM classes WHERE is_active = false"""
    elif historical == True:
        sql = """SELECT * FROM classes WHERE date < CURRNET_DATE"""
    else:
        sql = """SELECT * FROM classes"""
    results = run_sql(sql)
    gym_classes = []
    if results:
        for row in results:
            name = row['name']
            class_date = date.fromisoformat(row['class_date'])
            class_time = time.fromisoformat(row['class_time'])
            capacity = row['capacity']
            is_active = row['is_active']
            id = row['id']
            gym_class = GymClass(name, class_date, class_time, capacity, is_active, id)
            gym_classes.append(gym_class)

# SAVE ONE
def save(gym_class: GymClass) -> GymClass:
    sql = """
            INSERT INTO classes
            (name, class_date, class_time, capacity, is_active) VALUES
            (%s, %s, %s, %s, %s)
            RETURNING *
            """
    values = [gym_class.name, 
              gym_class.class_date.isoformat(), 
              gym_class.class_time.isoformat(), 
              gym_class.capacity, 
              gym_class.is_active]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        gym_class.id = result['id']
        return gym_class

# DELETE ONE
def delete(id: int) -> None:
    sql = """
            DELETE
            FROM classes
            WHERE id = %s
            """
    values = [id]
    run_sql(sql, values)

# DELETE ALL
def delete_all() -> None:
    sql = """
            DELETE
            FROM classes
            """
    run_sql(sql)

# UPDATE ONE
def update(gym_class: GymClass) -> None:
    sql = """
            UPDATE classes
            SET (name, class_date, class_time, capacity, is_active) = (%s, %s, %s, %s, %s)
            WHERE id = %s
            """
    values = [gym_class.name, 
              gym_class.class_date.isoformat(), 
              gym_class.class_time.isoformat(), 
              gym_class.capacity, 
              gym_class.is_active, 
              gym_class.id]
    run_sql(sql, values)

# Return all members booked onto a gym_class
def get_all_booked_members(id: int) -> list[Member]:
    sql = """
            SELECT m.*
            FROM bookings b
            INNER JOIN members m
            ON b.member_id = m.id
            WHERE b.class_id = %s
            """
    values = [id]
    results = run_sql(sql, values)
    members = []
    if results:
        for row in results:
            first_name = row['first_name']
            last_name = row['last_name']
            is_premium = row['is_premium']
            is_active = row['is_active']
            id = row['id']
            member = Member(first_name, last_name, is_premium, is_active, id)
            members.append(member)
    return members
