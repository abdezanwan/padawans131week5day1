from flask import Flask, render_template
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route("/")
def index():
    return "Hello from Flask!"

@app.route("/html")
def index_html():
    happy_family= ["Samer", "Sajid", "Sidra", "Safa", "Rahiem"]
    return render_template("index.html", message="This is all I have in this life", red=True, html_people=happy_family)

