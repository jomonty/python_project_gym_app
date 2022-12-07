from datetime import datetime

from db.run_sql import run_sql
from models.news import News

# RESULT PARSER
def results_parser(results):
    news_list = []
    for row in results:
        news_item = row['news_item']
        create_date = row['create_date']
        id = row['id']
        news = News(news_item, create_date, id)
        news_list.append(news)
    return news_list

# SELECT ONE
def select(id: int) -> News:
    sql = """
            SELECT *
            FROM news
            WHERE id = %s
            """
    values = [id]
    results = run_sql(sql, values)
    if results:
        news = results_parser(results)[0]
        return news

# SELECT ALL
def select_all() -> list[News]:
    sql = """
            SELECT *
            FROM news
            ORDER BY create_date DESC
            """
    results = run_sql(sql)
    return results_parser(results)

# SELECT LATEST x
def select_latest_x(x: int) -> list[News]:
    sql = """
            SELECT *
            FROM news
            ORDER BY create_date DESC
            LIMIT %s
            """
    values = [x]
    results = run_sql(sql, values)
    return results_parser(results)

# SAVE ONE
def save_one(news: News) -> News:
    sql = """
            INSERT
            INTO news (news_item)
            VALUES (%s)
            RETURNING *
            """
    values = [news.news_item]
    results = run_sql(sql, values)
    if results:
        news = results_parser(results)[0]
    return news

# UPDATE ONE
def update_one(news: News) -> News:
    sql = """
            UPDATE news
            SET (news_items) = (%s)
            WHERE id = %s
            """
    values = [news.news_item, news.id]
    run_sql(sql, values)

# DELETE ONE
def delete_one(id: int) -> None:
    sql = """
            DELETE
            FROM news
            WHERE id = %s
            """
    values = [id]
    run_sql(sql, values)

# DELETE ALL
def delete_all() -> None:
    sql = """
            DELETE
            FROM news
            """
    run_sql(sql)