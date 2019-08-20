# Flask Introduction

## Project Aims
* Create a Fan Page for Thorin and Company

## Developer Aims - learn how to:
* Create and run a Flask project
* Serve HTML/CSS/JS from the back end
* Make code re-usable by using template logic
* Use Jinja templating language to achieve above
* Use forms to take data from client and pass to server
* Post data from a HTML form to the backend
* Deploy a Flask project using Heroku

## Approach

### Setup using VS Code on a Mac
**sudo pip3 install Flask** used to install Flask
**python3 -m venv env** to install virtual environment in that folder
Open command pallette, type **Python: Select Interpreter** and select the virtual environment in your project folder that starts with *./env* or *.\env*
In command pallette, run Terminal: **Create New Integrated Terminal**
Install Flask in the virtual environment with **pip3 install Flask**
Create app.py (In flask, the convention is to use run.py or app.py)
**from flask import Flask** to import Flask. Capital F indicates a class name.
Create instance of flash within app.py with **app = Flask(__name__)**

In Terminal **python3 -m flask run** to run the app and serve

### Rendering html
Import the **render_template** function from Flask and use this to render files eg index.html
Html files saved in templates folder for Flask conventions.

### Resources and reference / support used
https://code.visualstudio.com/docs/python/tutorial-flask