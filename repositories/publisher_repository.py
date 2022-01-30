from db.run_sql import run_sql

from models.publisher import Publisher
from models.book import Book
import repositories.publisher_repository as publisher_repository
import repositories.book_repository as book_repository

def save(publisher):
    sql = "INSERT INTO publishers (name, location, active) VALUES (%s, %s, %s) RETURNING *"
    values = [publisher.name, publisher.location, publisher.active]
    results = run_sql(sql, values)
    id = results[0]['id']
    publisher.id = id
    return publisher

def delete_all():
    sql = "DELETE  FROM publishers"
    run_sql(sql)

def delete_publisher(publisher):
    sql = "DELETE  FROM publishers WHERE id = %s"
    values = [publisher.id]
    run_sql(sql, values)

def select_all():
    publishers = []

    sql = "SELECT * FROM publishers"
    results = run_sql(sql)

    for row in results:
        publisher = Publisher(row["name"], row["location"], row["id"] )
        publishers.append(publisher)
    return publishers