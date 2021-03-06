import os
import json
from flask import Flask, render_template, request, flash

# Create an instance, store in a variable called app.
# __name__ is a built in variable to tell flask where to look for files
app = Flask(__name__)
app.secret_key = 'something_very_secret'

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", list_of_numbers=[1, 2, 3], company=data)

@app.route("/about/<member_name>")
def about_member(member_name):
    member = {}

    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj

    return render_template("member.html", member=member)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have received your message and will translate it into dwarf runes before replying shortly by scratching a rune on your front door.".format(request.form["name"]))
        print("POST Method used on contact page.")
        print(request.form)
        # could used request.form["name"] to access the dictionary in the request.form data
    return render_template("contact.html", page_title="Contact Us")

@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers at Thorin & Company")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)