from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.book import Book
from repositories import book_repository
from repositories import publisher_repository

books_blueprint = Blueprint("/books", __name__)

@books_blueprint.route("/books")
def list_books():
    books = book_repository.select_all()
    return render_template("books/index.html", all_books = books)

