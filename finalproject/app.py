# import important libraries
from flask import Flask, render_template, request, redirect, flash, session
from cs50 import SQL
from flask_session import Session

# app for flask
app = Flask(__name__)

# app configuration
app.config["TEMPLATES_AUTO_RELOAD"] = True

# sql for future improvements
db = SQL("sqlite:///base.db")

# main router


@app.route("/")
# @login_required
def index():
    return render_template("index.html")

# products


@app.route("/products")
# @login_required
def products():
    return render_template("products.html")

# cart/docs


@app.route("/cart")
# @login_required
def cart():
    return render_template("cart.html")

# about


@app.route("/about")
# @login_required
def about():
    return render_template("about.html")

# contact


@app.route("/contact")
# @login_required
def contact():
    return render_template("contact.html")
