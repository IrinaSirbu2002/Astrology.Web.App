#from request import lookup, add_days
import os

from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
import sqlite3
import csv

#print(lookup("2023-08-02"))

# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/distcalc", methods=["GET", "POST"])
def distcalc():
    with open("distances.csv", "r") as file:
        reader = csv.DictReader(file)
        if request.method == "POST":
            dist1 = request.form.get("place1")
            dist2 = request.form.get("place2")
            for row in reader:
                if (dist1 == row["place1"] or dist1 == row["place2"]) and (dist2 == row["dist1"] or dist2 == row["dist2"]):
                    return render_template("calculated.html", distances=reader)
                    
        else:
            return render_template("distcalc.html", distances=reader)

@app.route("/neo")
def neo():
    return render_template("index.html")

@app.route("/apod")
def apod():
    return render_template("index.html")

@app.route("/images")
def images():
    return render_template("index.html")