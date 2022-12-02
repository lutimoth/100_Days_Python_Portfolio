from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

db = sqlite3.connect("books-collection.db")
cursor = db.cursor()

cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, \
    author varchar(250) NOT NULL, \
    rating FLOAT NOT NULL)")

all_books = []

@app.route('/')
def home():
    return render_template('index.html', books=all_books)


@app.route("/add", methods=["GET","POST"])
def add():
    book_info = {
        'name': request.form.get('book_name'),
        'author': request.form.get('book_author'),
        'rating': request.form.get('rating')
    }
    all_books.append(book_info)
    print(all_books)
    return render_template('add.html')


if __name__ == "__main__":
    app.run(debug=True)

