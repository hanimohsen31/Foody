import os
from types import MethodType
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
import random
# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///food.db")

# ----------------------------------------------- index ----------------------------------------------- #
@app.route("/",methods=["GET", "POST"])
def index():
    if request.method == "POST":
        search = request.form.get("search")
        print(search)
        rows = db.execute("SELECT * FROM food WHERE title like ? ", '%'+search+'%')
        if rows :
            rows = db.execute("SELECT * FROM food WHERE title like ? ", '%'+search+'%')
            return render_template("card.html" , data=rows )
        else:
            return redirect("/")
        
    if request.method == "GET":
            return render_template("index.html")

# ----------------------------------------------- view ----------------------------------------------- #
@app.route("/view" ,methods=["GET", "POST"] )
def view():
    if request.method == "POST":
      pass

    if request.method == "GET":
        rows = db.execute("SELECT * FROM food WHERE type = ?", 'dinner')
        random_choice = int(random.randint(0,len(rows)))
        row = rows[random_choice]
        v = row['link'].split('v=')[1]
        return render_template("view.html" , data=row ,src=v)
# -------------------------------------------- week ----------------------------------------------------- #
@app.route("/week")
def week():
    if request.method == "POST":
        pass

    if request.method == "GET":
        rows = db.execute("SELECT * FROM food WHERE type = ?", 'dinner')
        list = random.sample(rows , len(rows))[1: 7]
        return render_template("table.html" , data=list)

# ----------------------------------------------- month ----------------------------------------------- #
@app.route("/month")
def month():
    if request.method == "POST":
        pass

    if request.method == "GET":
        rows = db.execute("SELECT * FROM food WHERE type = ?", 'dinner')
        list = random.sample(rows , len(rows))[1: 30]
        return render_template("table.html" , data=list)

# ----------------------------------------------- fast -------------------------------------------------- #
@app.route("/fast")
def fast():
    if request.method == "POST":
        pass

    if request.method == "GET":
        rows = db.execute("SELECT * FROM food WHERE type = ?", 'salty')
        return render_template("table.html" , data=rows)
# ----------------------------------------------- dessert ----------------------------------------------- #
@app.route("/dessert")
def dessert():
    if request.method == "POST":
        pass

    if request.method == "GET":
        rows = db.execute("SELECT * FROM food WHERE type = ?", 'dessert')
        return render_template("table.html" , data=rows)
# ----------------------------------------------- all ----------------------------------------------- #
@app.route("/all",methods=["GET", "POST"])
def all():
    if request.method == "POST":
        pass

    if request.method == "GET":
        rows = db.execute("SELECT * FROM food ")
        return render_template("card.html" , data=rows)

# ---------------------------------------------------------------------------------------------- # 
