from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1> Guess a number between 0 and 9</h1>'\
        '<p> Change the number at the end of the url! </p>' \
        '<img src="https://media0.giphy.com/media/xUn3CftPBajoflzROU/giphy.gif?cid=ecf05e475z2ewinp1pqc8k1kjog285rg9of39e37q2zt6xjh&rid=giphy.gif&ct=g">'

number = random.choice(range(0,10))

@app.route('/<int:guess>')
def check_number(guess):
    if guess < number:
        return '<h1 style="text-color:red"> Too low! </h1>'\
                '<img src="https://media2.giphy.com/media/W0c3xcZ3F1d0EYYb0f/giphy.gif?cid=ecf05e47f71cgo9zvlbqp9irylqg986308civb7ctd032utw&rid=giphy.gif&ct=g">'
    if guess > number:
        return '<h1 style="text-color:pink"> Too high! </h1>'\
                '<img src="https://media1.giphy.com/media/QW419eoB9mEZncyZZm/giphy.gif?cid=ecf05e47ryp4qtu9yip6jjpd2sz2924xew3kz3g89sgm4svg&rid=giphy.gif&ct=g">'
    if guess == number:
        return '<h1 style="text-color:green"> You got it! </h1>'\
            '<img src="https://media4.giphy.com/media/3oz8xAFtqoOUUrsh7W/giphy.gif?cid=ecf05e47waemi4e7xfyaporhmel3x4ir6o4vprbe7xov0vdu&rid=giphy.gif&ct=g">'

if __name__ == "__main__":
    app.run(debug=True)