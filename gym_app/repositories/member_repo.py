from db.run_sql import run_sql
from models.member import Member
from models.gym_class import GymClass

# SELECT ONE
def select(id: int) -> Member:
    sql = """
            SELECT *
            FROM members
            WHERE id = %s
            """
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        first_name = result['first_name']
        last_name = result['last_name']
        is_premium = result['is_premium']
        is_active = result['is_active']
        member = Member(first_name, last_name, is_premium, is_active, id)
        return member

# SELECT ALL
def select_all() -> list[Member]:
    sql = """
            SELECT *
            FROM members
            """
    results = run_sql(sql)
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

# SAVE ONE
def save(member: Member) -> Member:
    sql = """
            INSERT INTO members
            (first_name, last_name, is_premium, is_active)
            VALUES
            (%s, %s, %s, %s)
            RETURNING *
            """
    values = [member.first_name, member.last_name, member.is_premium, member.is_active]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        member.id = result['id']
        return member
    
# DELETE ONE
def delete(id: int) -> None:
    sql = """
            DELETE
            FROM members
            WHERE id = %s
            """
    values = [id]
    run_sql(sql, values)

# DELETE ALL
def delete_all() -> None:
    sql = """
            DELETE
            FROM members
            """
    run_sql(sql)

# UPDATE ONE
def update(member: Member) -> None:
    sql = """
            UPDATE members
            SET (first_name, last_name, is_premium, is_active) = (%s, %s, %s, %s)
            WHERE id = %s
            """
    values = [member.first_name, member.last_name, member.is_premium, member.is_active, member.id]
    run_sql(sql, values)

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
    gym_classes = []
    if results:
        for row in results:
            name = row['name']
            class_date = row['class_date']
            class_time = row['class_time']
            capacity = row['capacity']
            is_active = row['is_active']
            id = row['id']
            gym_class = GymClass(name, class_date, class_time, capacity, is_active, id)
            gym_classes.append(gym_class)
    return gym_classes
    