from datetime import date, time
from db.run_sql import run_sql
from models.gym_class import GymClass
from models.member import Member

def results_parser(results: dict) -> list[GymClass]:
    gym_classes = []
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
        
# SELECT ONE
def select(id: int) -> GymClass:
    sql = """
            SELECT *
            FROM classes
            WHERE id = %s
            """
    values = [id]
    results = run_sql(sql, values)
    gym_classes = results_parser(results)
    if gym_classes:
        return gym_classes[0]

# SELECT ALL
def select_all():
    sql = """
            SELECT *
            FROM classes
            """
    results = run_sql(sql)
    gym_classes = results_parser(results)
    return gym_classes

# SELECT ALL UPCOMING
def select_all_upcoming():
    sql = """
            SELECT *
            FROM classes
            WHERE class_date >= CURRENT_DATE and is_active = true
            """
    results = run_sql(sql)
    gym_classes = results_parser(results)
    return gym_classes

# SELECT ALL HISTORIC
def select_all_historic():
    sql = """
            SELECT *
            FROM classes
            WHERE class_date < CURRENT_DATE
            """
    results = run_sql(sql)
    gym_classes = results_parser(results)
    return gym_classes

# SELECT ALL INACTIVE
def select_all_inactive():
    sql = """
            SELECT *
            FROM classes
            WHERE is_active = false
            AND class_date >= CURRENT_DATE
            """
    results = run_sql(sql)
    gym_classes = results_parser(results)
    return gym_classes
    
# SELECT ALL BY NAME
def select_all_upcoming_by_name(class_name):
    sql = """
            SELECT *
            FROM classes
            WHERE name = %s 
            AND class_date >= CURRENT_DATE
            AND is_active = true
            """
    values = [class_name]
    results = run_sql(sql, values)
    gym_classes = results_parser(results)
    return gym_classes

# SELECT ALL CLASS NAMES
def select_distinct_classes() -> list[str]:
    sql = """
            SELECT DISTINCT name
            FROM classes"""
    results = run_sql(sql)
    distinct_classes = []
    for row in results:
        distinct_classes.append(row['name'])
    return distinct_classes

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
