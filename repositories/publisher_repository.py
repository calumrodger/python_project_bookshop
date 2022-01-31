import pdb
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

def delete_publisher(id):
    sql = "DELETE  FROM publishers WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def select_all():
    publishers = []

    sql = "SELECT * FROM publishers"
    results = run_sql(sql)

    for row in results:
        publisher = Publisher(row["name"], row["location"], row["active"], row["id"])
        publishers.append(publisher)
    return publishers

def select(id):
    publisher = None
    sql = "SELECT * FROM publishers WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        publisher = Publisher(result["name"], result["location"], result["active"], result["id"])
    return publisher

def switch_active(id):
    sql = "UPDATE publishers SET (active) = (%s) WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(publisher):
    sql = "UPDATE publishers SET (name, location, active) = (%s, %s, %s) WHERE id = %s"
    values = [publisher.name, publisher.location, publisher.active, publisher.id]
    run_sql(sql, values)

# !! COME BACK TO THIS IF YOU HAVE TIME
# def switch_active_status(publisher):
#     if publisher.active == True:
#         sql = "UPDATE publishers SET active = False WHERE id = %s"
#     else:
#         sql = "UPDATE publishers SET active = True WHERE id = %s"
#     publisher = [publisher.active]
#     pdb.set_trace()
#     run_sql(sql, publisher)