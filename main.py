from flask import Flask, render_template
import requests

blog_posts = requests.get("https://api.npoint.io/88c2c1f644ef334058be")
post_json = blog_posts.json()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html', posts=post_json)

@app.route("/posts/<int:id>")
def post(id):
    return render_template('post.html', post=post_json[id - 1])

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)