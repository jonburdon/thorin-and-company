# Flask Introduction

Project created following tutorial followed from the Code Institute. Adapted to use VSCode on a mac instead of AWS Cloud9 as used in the tutorial.
This readme file is the developers own documentation for the learning project.

## Project Aims
* Create a Fan Page for Thorin and Company

## Developer Aims - learn how to:
* Create and run a Flask project
* Serve HTML/CSS/JS from the back end
* Make code re-usable by using template logic
* Use Jinja templating language to achieve above
* Use template inheritance to keep identical navbar across all pages.
* Add pages and integrate data
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


### Routing
Add routing using / for index.html and /about for about.html
Refactor to include three views and routes, using Jinja templating to direct to corresponding html files.

### Inheritance
Use inheritance to set up template for header area and pass content in to the template.

### Styling
Applied a bootstrap theme by downloading from startbootstrap.com and adding custom Jinja code to link to files.

### Content
Added some content from Lord of The Rings Wiki using Bootstrap classes.
Refactor to pass page titles from app.py to each page, to be displayed within h2 tags.


### Logic
Add list data 1,2,3 to app.py and use a for loop on about.html to display this data in three <p> tags.


### Resources and reference / support used
VSCode setup Instructions:
https://code.visualstudio.com/docs/python/tutorial-flask

Bootstrap template from:
https://startbootstrap.com/themes/clean-blog/

Text content from:
https://lotr.fandom.com/wiki/Thorin_and_Company