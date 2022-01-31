from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.book import Book
from repositories.book_repository import book_repository
from repositories.publisher_repository import publisher_repository
import pdb

books_blueprint = Blueprint("/books", __name__)

@books_blueprint.route("/books")
def list_books():
    books = book_repository.select_all()
    return render_template("books/index.html", all_books = books)

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

@books_blueprint.route("/books/<id>", methods=['POST'])
def update_book(id):
    # pdb.set_trace()
    title = request.form["title"]
    publisher_id = request.form["publisher_id"]
    author = request.form["author"]
    genre = request.form["genre"]
    stock = request.form["stock"]
    cost_price = request.form["cost_price"]
    sale_price = request.form["sale_price"]
    blurb = request.form["blurb"]
    publisher = publisher_repository.select(publisher_id)
    book = Book(title, publisher, author, genre, stock, cost_price, sale_price, blurb, id)
    
    book_repository.update(book)
    return redirect ("/books/<id>")

@books_blueprint.route("/tasks/<id>/edit", methods=['GET'])
def edit_book(id):
    book = book_repository.select(id)
    publishers = publisher_repository.select_all()
    return render_template('books/edit.html', book=book, all_publishers=publishers)