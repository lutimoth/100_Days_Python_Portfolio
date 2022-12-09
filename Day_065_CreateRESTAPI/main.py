from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)
    
    def to_dict(self, name=True):
        if name == False:
           return {column.name: getattr(self, column.name) for column in self.__table__.columns if column.name != 'name'}
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")

## HTTP GET - Read Record
@app.route("/random", methods=["GET"])
def random_cafe():
    cafes = Cafe.query.all()
    rand_cafe = random.choice(cafes)
    return jsonify(cafe=rand_cafe.to_dict())

@app.route("/all")
def all_cafe():
    cafes = Cafe.query.all()
    return jsonify(cafes={cafe.name: cafe.to_dict(name=False) for cafe in cafes})


@app.route("/search")
def find_cafe():
    area = request.args.get('location')
    print(area)
    cafe_query = Cafe.query.where(Cafe.location == area)
    print(cafe_query)
    if cafe_query.first() is None:
        return jsonify(error={"Not Found":"Sorry, we don't have a cafe at that location."})
    return jsonify(cafes={cafe.name: cafe.to_dict(name=False) for cafe in cafe_query})


## HTTP POST - Create Record
@app.route("/add", methods=["GET", "POST"])
def add_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
