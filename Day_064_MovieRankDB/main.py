from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '962d4be7548f3717c95be162685a09d4'
MOVIE_DB_API_KEY = '962d4be7548f3717c95be162685a09d4'
MOVIE_DB_SEARCH_URL = 'https://api.themoviedb.org/3/search/movie'
MOVIE_DB_INFO_URL = "https://api.themoviedb.org/3/movie"
MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"

Bootstrap(app)

## -- DATABASE MAKER -- ##
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Springboard_GIT/100_Days_Python_Portfolio/Day_064_MovieRankDB/movie-collection.db'
app.config['SQLACHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
#print(db)

##TABLE CREATOR
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(250), unique = True, nullable = False)
    year = db.Column(db.String(250), unique = False, nullable = False)
    description = db.Column(db.String(250), unique = True, nullable = False)
    rating = db.Column(db.Float, nullable = True)
    ranking = db.Column(db.Integer, nullable = True)
    review = db.Column(db.String(250), unique = True, nullable = True)
    img_url = db.Column(db.String(250), unique = True, nullable = False)

db.create_all()

# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )

# db.session.add(new_movie)
# db.session.commit()

all_movies = []

class RateMovieForm(FlaskForm):
    rating = StringField("Your Rating Out of 10 e.g. 7.5")
    review = StringField("Your Review")
    submit = SubmitField("Done")

class FindMovieForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")

@app.route("/")
def home():
    all_movies = Movie.query.order_by(Movie.rating.desc()).all()
    for i in range(len(all_movies)):
        all_movies[i].ranking = i+1
    db.session.commit()
    #print(all_movies)
    return render_template("index.html", movies=all_movies)

@app.route("/edit", methods=["GET","POST"])
def edit():
    form = RateMovieForm()
    movie_id = request.args.get("id")
    movie = Movie.query.get(movie_id)
    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", movie=movie, form=form)

@app.route('/delete')
def delete_movie():
    movie_id = request.args.get("id")
    movie = Movie.query.get(movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/add',methods=["GET","POST"])
def add_movie():
    form = FindMovieForm()
    if form.validate_on_submit():
        movie_title = form.title.data
        movies = requests.get(MOVIE_DB_SEARCH_URL, params={"api_key": MOVIE_DB_API_KEY, "query": movie_title})
        movie_options = movies.json()['results']
        #print(movie_options)
        return render_template("select.html", movie_options=movie_options)
    return render_template("add.html", form=form)

@app.route("/find")
def find_movie():
    movie_api_id = request.args.get("id")
    if movie_api_id:
        movie_api_url = f"{MOVIE_DB_INFO_URL}/{movie_api_id}"
        response = requests.get(movie_api_url, params={"api_key": MOVIE_DB_API_KEY, "language": "en-US"})
        data = response.json()
        new_movie = Movie(
            title=data["title"],
            year = data["release_date"].split("-")[0],
            img_url = f"{MOVIE_DB_IMAGE_URL}{data['poster_path']}",
            description = data["overview"]
        )
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for("edit", id=new_movie.id))
if __name__ == '__main__':
    app.run(debug=True)
