from flask import Flask, render_template, request
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

# @app.route("/contact")
@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]
        print(f"{name}\n{email}\n{phone}\n{message}")
        send_email(name, email, phone, message)
        return render_template('contact.html', msg_sent=True)
    return render_template('contact.html', msg_sent=False)

def send_email(name, email, phone, message):
    import smtplib
    import os

    user = os.environ["MAILTRAP_UN"]
    pw = os.environ["MAILTRAP_PW"]

    sender = "Private Person <from@example.com>"
    receiver = "A Test User <to@example.com>"

    message = f"""Subject: Hi Mailtrap\nTo: {receiver}\nFrom: {sender}\n
    {name}\n{email}\n{phone}\n{message}""".encode("utf-8")
    print(f"user: {user}, password {pw}")

    with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
        server.set_debuglevel(1)
        server.starttls()
        server.login(user, pw)
        server.sendmail(sender, receiver, message)

if __name__ == "__main__":
    app.run(debug=True)