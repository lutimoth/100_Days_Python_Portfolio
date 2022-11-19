from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1> Guess a number between 0 and 9</h1>'\
        '<img src="https://media0.giphy.com/media/xUn3CftPBajoflzROU/giphy.gif?cid=ecf05e475z2ewinp1pqc8k1kjog285rg9of39e37q2zt6xjh&rid=giphy.gif&ct=g">'

if __name__ == "__main__":
    app.run(debug=True)