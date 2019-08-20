import os
from flask import Flask

# Create an instance, store in a variable called app.
# __name__ is a built in variable to tell flask where to look for files
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=True)