from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.book import Book
from repositories.book_repository import book_repository
from repositories.publisher_repository import publisher_repository

books_blueprint = Blueprint("/books", __name__)

@books_blueprint.route("/books")
def list_books():
    books = book_repository.select_all()
    return render_template("books/index.html", all_books = books)

@books_blueprint.route("/books/<id>/delete", methods=['GET', 'POST'])
def remove_book(id):
    book_repository.delete_book(id)
    return redirect("/books")

@books_blueprint.route("/books/<id>/sell", methods=['GET', 'POST'])
def sell_book(id):
    book_repository.sell_copy(id)
    return redirect("/books")