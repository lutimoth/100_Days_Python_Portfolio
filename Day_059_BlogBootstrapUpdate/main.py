from flask import Flask, render_template
import requests

app = Flask(__name__)

response = requests.get('https://api.npoint.io/908ee30b5c1c9a2037f6')
blog_posts = response.json()

@app.route('/')
def home():
    return render_template('index.html', all_posts=blog_posts)

@app.route('/about.html')
def about_page():
    return render_template('about.html')

@app.route('/contact.html')
def contact_page():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)
