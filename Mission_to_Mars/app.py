from flask import Flask, render_template, redirect, jsonify
from flask_pymongo import PyMongo 
import scrape_mars

app= Flask(__name__)
mongo= PyMongo(app, uri="mongodb://localhost:27017/mars_db")

@app.route("/")
def home():
    mars_db = mongo.db.collection.find_one()
    return render_template("index.html", mars=mars_db)

@app.route("/scrape")
def scrape():
    data = scrape_mars.scrape()
    mongo.db.collection.update({}, data, upsert=True)
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)



dump(mars_db)