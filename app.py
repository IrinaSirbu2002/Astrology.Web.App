from request import add_days, api_apod, lookup
from datetime import datetime
from flask import Flask, render_template, request
import csv

# Configure application
app = Flask(__name__)

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


@app.route("/neo", methods=["GET", "POST"])
def neo():
    neo_data_dict = []
    if request.method == "POST":
        try:
            date = request.form.get("date")
            frmdate = datetime.strptime(date, '%Y-%m-%d')
            if date == '':
                return render_template("neo.html", x=2)
        except ValueError:
            return render_template("neo.html", x=1)
        
        formdate = frmdate.strftime("%Y-%m-%d")
        neo_data = lookup(formdate)
        # converting each row to a dictionary
        for row in neo_data:
            data = {
                "name": row[1],
                "size": row[2],
                "date": row[3],
                "miss_distance": row[4]
            }
            neo_data_dict.append(data)

        return render_template("neocalc.html", asteroids=neo_data_dict, date=formdate)
        
    else:
        return render_template("neo.html", x=0)

@app.route("/apod")
def apod():
    apod_info = api_apod()
    title = apod_info.get("title")
    image_url = apod_info.get("image_url")
    explanation = apod_info.get("explanation")
    return render_template("apod.html", title=title, image_url=image_url, explanation=explanation)
