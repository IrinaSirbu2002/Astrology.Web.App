from request import add_days, api_apod, lookup
import os

from flask import Flask, flash, redirect, render_template, request, send_from_directory
from flask_session import Session
import csv

# Configure application
app = Flask(__name__)

# @app.route('/favicon.ico')
# def favicon():
#     return send_from_directory(app.static_folder, 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/distcalc", methods=["GET", "POST"])
def distcalc():
    distances = []
    places = []
    with open("distances.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            distances.append(row)
        for distance in distances:
                if distance["place1"] not in places:
                    places.append(distance["place1"])
        if request.method == "POST":
            dist1 = request.form.get("place1")
            dist2 = request.form.get("place2")
            for distance in distances:
                if (dist1 in [distance["place1"], distance["place2"]]) and (dist2 in [distance["place1"], distance["place2"]]):
                    return render_template("calculated.html", distance=distance)
            return render_template("distcalc.html", places=places)

        else:
            return render_template("distcalc.html", places=places)

@app.route("/neo")
def neo():
    if request.method == "POST":
        date = request.form.get()
        neo_data = lookup(date)
        return render_template("neo.html")
    else:
        return render_template("neo.html")

@app.route("/apod")
def apod():
    apod_info = api_apod()
    title = apod_info.get("title")
    image_url = apod_info.get("image_url")
    explanation = apod_info.get("explanation")
    return render_template("apod.html", title=title, image_url=image_url, explanation=explanation)
