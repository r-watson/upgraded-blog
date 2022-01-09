# POST Request with HTML form 

The form is submitted and grabbed by the receive_data() function using the request method from Flask. Reference the POST as a dictionary. The "name" field from HTML is the key. The user input is the value.
```python
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def receive_data():
    username = request.form['submitted-name']
    password = request.form['submitted-password']
    return f"<h1>Name: {username}, Password: {password}</h1>"

if __name__ == "__main__":
    app.run(debug=True)
```

NOTE: The action attribute of the form can be set to "/login" e.g.

```html
<form action="/login" method="post">
```
or it can be dynamically generated with url_for e.g.
```html
<form action="{‌{ url_for('receive_data') }}" method="post">
```
Depending on where your server is hosted, the "/login" path may change. So it's usually a better idea to use url_for to dynamically generate the url for a particular function in your Flask server.

Use the following to submit form with assigned names.
```html
    <form action="/login" method="post">
        <label>Name
            <input name="submitted-name" placeholder="name">
        </label>
        <label>Password
            <input name="submitted-password" placeholder="password">
        </label>
        <button type="submit">Ok</button>
    </form>
```

[Flask Tutorial Video on HTTP Methods Get/Post](https://www.youtube.com/watch?v=9MHYHgh4jYc&list=PLzMcBGfZo4-n4vJJybUVV3Un_NFS5EOgX&index=5)

[From 100 Days of Code - Day 60 - Make Post Requests with HTML Forms](https://www.udemy.com/course/100-days-of-code/learn/lecture/22389734#questions)

# Jinja formatting in HTML

The following HTML looks at the msg_sent variable passed from Flask and see if it's true or false. It displays HTML accordingly.

```html
            {% if msg_sent: %}
            <h1>Successfully sent your message</h1>
            {% else: %}
            <h1>Contact Me</h1>
            {% endif %}
```

The following Flask decorator/Python function returns the rendered HTML page depening on if it was a POST or GET request.

```python
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        print(data["name"])
        print(data["email"])
        print(data["phone"])
        print(data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)
```