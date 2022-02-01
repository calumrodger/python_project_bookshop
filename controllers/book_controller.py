from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.book import Book
from models.publisher import Publisher
from repositories.book_repository import book_repository
from repositories.publisher_repository import publisher_repository
import pdb

books_blueprint = Blueprint("/books", __name__)

@books_blueprint.route("/books")
def list_books():
    books = book_repository.select_all()
    publishers = publisher_repository.select_all()
    genres = book_repository.list_all_genres()
    authors = book_repository.list_all_authors()
    return render_template("/books/index.html", all_books = books, all_publishers = publishers, all_genres=genres, all_authors=authors)



@books_blueprint.route("/books/<id>", methods=["GET"])
def show_books(id):
    book = book_repository.select(id)
    return render_template("books/show.html", book=book)

@books_blueprint.route("/books/<id>/delete", methods=['GET'])
def remove_book(id):
    book_repository.delete_book(id)
    return redirect("/books")

@books_blueprint.route("/books/<id>/sell", methods=['GET'])
def sell_book(id):
    book_repository.sell_copy(id)
    return redirect("/books")

@books_blueprint.route("/books/<id>/buy", methods=['GET'])
def buy_book(id):
    book_repository.buy_copy(id)
    return redirect("/books")

@books_blueprint.route("/books/<id>", methods=['GET'])
def edit_book(id):
    book = book_repository.select(id)
    publishers = publisher_repository.select_all()
    return render_template('books/show.html', book=book, all_publishers=publishers)

@books_blueprint.route("/books/<id>", methods=['POST'])
def update_book(id):
    title = request.form["title"]
    publisher_id = request.form["publisher_id"]
    author = request.form["author"]
    genre = request.form["genre"]
    stock = request.form["stock"]
    cost_price = request.form["cost_price"]
    sale_price = request.form["sale_price"]
    blurb = request.form["blurb"]
    image = request.form["image"]
    publisher = publisher_repository.select(publisher_id)
    book = Book(title, publisher, author, genre, stock, cost_price, sale_price, blurb, image, id)
    book_repository.update(book)
    return redirect ("/books/" + id)



@books_blueprint.route("/books/new", methods=['POST'])
def create_book():
    title = request.form["title"]
    publisher_id = request.form["publisher_id"]
    author = request.form["author"]
    genre = request.form["genre"]
    stock = request.form["stock"]
    cost_price = request.form["cost_price"]
    sale_price = request.form["sale_price"]
    blurb = request.form["blurb"]
    image = request.form["image"]
    publisher = publisher_repository.select(publisher_id)
    book = Book(title, publisher, author, genre, stock, cost_price, sale_price, blurb, image, id)
    book_repository.save(book)
    return redirect ("/books")

@books_blueprint.route("/books/new", methods=['GET'])
def new_book():
    publishers = publisher_repository.select_all()
    return render_template('books/new.html', all_publishers=publishers)  


@books_blueprint.route("/books/byauthor", methods=['POST'])
def search_for_author():
    search_term = request.form["author"]
    books = book_repository.select_by_author(search_term)
    publishers = publisher_repository.select_all()
    genres = book_repository.list_all_genres()
    authors = book_repository.list_all_authors()
    return render_template("books/byauthor.html", all_books=books, all_publishers=publishers, all_genres=genres, all_authors=authors)

@books_blueprint.route("/books/bygenre", methods=['POST'])
def search_for_genre():
    search_term = request.form["genre"]
    pdb.set_trace()
    books = book_repository.select_by_genre(search_term)
    publishers = publisher_repository.select_all()
    genres = book_repository.list_all_genres()
    authors = book_repository.list_all_authors()
    return render_template("/books/bygenre.html", all_books=books, all_publishers=publishers, all_genres=genres, all_authors=authors)

