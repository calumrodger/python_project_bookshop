from db.run_sql import run_sql

from models.book import Book
from models.publisher import Publisher
import repositories.book_repository as book_repository
import repositories.publisher_repository as publisher_repository

def save(book):
    sql = "INSERT INTO books (title, publisher_id, author, genre, stock, cost_price, sale_price, blurb) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING *"
    values = [book.title, book.publisher.id, book.author, book.genre, book.stock, book.cost_price, book.sale_price, book.blurb]
    results = run_sql(sql, values)
    id = results[0]['id']
    book.id = id
    return book

def delete_all():
    sql = "DELETE  FROM books"
    run_sql(sql)

def delete_book(id):
    sql = "DELETE  FROM books WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def select_all():
    books = []

    sql = "SELECT * FROM books"
    results = run_sql(sql)

    for row in results:
        book = Book(row["title"], row["publisher_id"], row["author"], row["genre"], row["stock"], row["cost_price"], row["sale_price"], row["blurb"], row["id"])
        books.append(book)
    return books

def select(id):
    book = None
    sql = "SELECT * FROM books WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        publisher = publisher_repository.select(result["publisher_id"])
        book = Book(result["title"], publisher, result["author"], result["genre"], result["stock"], result["cost_price"], result["sale_price"], result["blurb"], result["id"])
    return book

def sell_copy(id):
        sql = "UPDATE books SET stock = stock - 1 WHERE id = %s"
        book = [id]
        run_sql(sql, book)

def update(book):
    sql = "UPDATE books SET (title, publisher_id, author, genre, stock, cost_price, sale_price, blurb) = (%s, %s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [book.title, book.publisher_id, book.author, book.genre, book.stock, book.cost_price, book.sale_price, book.blurb, book.id]
    run_sql(sql, values)