from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.book import Book
from repositories import book_repository
from repositories import publisher_repository

publishers_blueprint = Blueprint("/publishers", __name__)

@publishers_blueprint.route("/publishers")
def list_publishers():
    publishers = publisher_repository.select_all()
    return render_template("publishers/index.html", all_publishers = publishers)

@publishers_blueprint.route("/publishers/<id>/active", methods=['GET', 'POST'])
def change_active(id):
    publisher_repository.switch_active(id)
    return redirect("/publishers")