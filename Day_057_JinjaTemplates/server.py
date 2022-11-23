from flask import Flask, render_template
from datetime import datetime
import requests

app = Flask(__name__)

@app.route('/')
def home():
    year = datetime.now().year
    return render_template("index.html", current_year = year)

@app.route(f'/guess/<name>')
def guess(name):
    year = datetime.now().year
    gender = requests.get('https://api.genderize.io', params={'name': name})
    age = requests.get('https://api.agify.io', params={'name': name})
    return render_template("guess.html", current_year = year)


if __name__ == "__main__":
    app.run(debug=True)