import os
from flask import Flask, render_template

# Create an instance, store in a variable called app.
# __name__ is a built in variable to tell flask where to look for files
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/careers")
def careers():
    return render_template("careers.html")


if __name__ == "__main__":
    app.run(debug=True)