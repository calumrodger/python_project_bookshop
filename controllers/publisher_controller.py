from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.book import Book
from models.publisher import Publisher
from repositories.book_repository import book_repository
from repositories.publisher_repository import publisher_repository

publishers_blueprint = Blueprint("/publishers", __name__)

@publishers_blueprint.route("/publishers")
def list_publishers():
    publishers = publisher_repository.select_all()
    return render_template("publishers/index.html", all_publishers = publishers)

@publishers_blueprint.route("/publishers/<id>/active", methods=['GET'])
def change_active(id):
    publisher_repository.switch_active(id)
    return redirect("/publishers")

@publishers_blueprint.route("/publishers/<id>", methods=['GET'])
def edit_publisher(id):
    publisher = publisher_repository.select(id)
    return render_template('publishers/show.html', publisher=publisher)

@publishers_blueprint.route("/publishers/<id>", methods=['POST'])
def update_publisher(id):
    # pdb.set_trace()
    name = request.form["name"]
    location = request.form["location"]
    active = request.form["active"]
    publisher = Publisher(name, location, active, id)
    
    publisher_repository.update(publisher)
    return redirect ("/publishers/" + id)

@publishers_blueprint.route("/publishers/new", methods=['GET'])
def new_publisher():
    return render_template("/publishers/new.html")

@publishers_blueprint.route("/publishers/new", methods=['POST'])
def create_publisher():
    name = request.form["name"]
    location = request.form["location"]
    active = request.form["active"]
    publisher = Publisher(name, location, active, id)
    publisher_repository.save(publisher)
    return redirect("/publishers")
