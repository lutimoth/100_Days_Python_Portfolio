# Beginning of Flask
from flask import Flask
app = Flask(__name__)

def make_bold(function):
    def bold_decorator():
        html = function()
        new_string = '<b>' + html + '</b>'
        return new_string
    return bold_decorator

def make_em(function):
    def em_decorator():
        html = function()
        new_string = '<em>' + html + '</em>'
        return new_string
    return em_decorator

def make_under(function):
    def under_decorator():
        html = function()
        new_string = '<u>' + html + '</u>'
        return new_string
    return under_decorator

@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>'\
        '<img src="https://media1.giphy.com/media/fUYNhyVEdVhCmMokf5/giphy.gif?cid=ecf05e478679775c99de512a96fc11fc504c890ebbe75373&rid=giphy.gif&ct=g" width=200> '

@app.route('/bye')
@make_bold
@make_em
@make_under
def bye():
    return 'Bye!'


@app.route('/<name>')
def greet(name):
    return f"Hello {name}!"


if __name__ == "__main__":
    app.run(debug=True)