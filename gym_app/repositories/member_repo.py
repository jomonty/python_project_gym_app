from datetime import date, time
from db.run_sql import run_sql
from models.member import Member
from models.gym_class import GymClass

# RESULTS PARSER
def results_parser(results):
    members = []
    if results == None or len(results) == 0:
        return members
    else:
        for row in results:
            first_name = row['first_name']
            last_name = row['last_name']
            is_premium = row['is_premium']
            is_active = row['is_active']
            id = row['id']
            member = Member(first_name, last_name, is_premium, is_active, id)
            members.append(member)
        return members

# SELECT ONE
def select(id: int) -> Member:
    sql = """
            SELECT *
            FROM members
            WHERE id = %s
            """
    values = [id]
    results = run_sql(sql, values)
    members = results_parser(results)
    if len(members) >= 1:
        return members[0]

# SELECT ALL
def select_all() -> list[Member]:
    sql = """
            SELECT *
            FROM members
            ORDER BY last_name ASC, first_name ASC
            """
    results = run_sql(sql)
    return results_parser(results)

# SELECT ALL ACTIVE
def select_all_active(active: bool = True) -> list[Member]:
    sql = """
            SELECT *
            FROM members
            WHERE is_active = %s
            ORDER BY last_name ASC, first_name ASC
            """
    values = [active]
    results = run_sql(sql, values)
    return results_parser(results)

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
    members = results_parser(results)
    if len(members) >= 1:
        member.id = members[0].id
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
    