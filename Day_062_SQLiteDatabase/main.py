from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

all_books = []


@app.route('/')
def home():
    return render_template('index.html')


@app.route("/add", methods=["GET","POST"])
def add():
    book_info = {
        'name': request.form.get('book_name'),
        'author': request.form.get('book_author'),
        'rating': request.form.get('rating')
    }
    all_books.append(book_info)
    return render_template('add.html')


if __name__ == "__main__":
    app.run(debug=True)

