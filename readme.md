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

### Working with data
Create company.json file which contains data on Thorin & Company (name, bio, image url)
Display the above in about.html
Iterate through json data to display each member of the company on the about.html page

### Template Logic
Add list data 1,2,3 to app.py and use a for loop on about.html to display this data in three <p> tags.
Use for loop to display data on each member.
Use if loop to check loop.index and display image on left or right of text for that member accordingly.
Add if loop to remove hr if loop.index is equal to 13.

### Advanced Routing
Use new route about/member_name to hyperlink each title to a page for that member.
Pass variable to routing to hyperlink each h3 to member data using variables.

### Handling form
Paste form from Bootstrap template.
Add method="POST" for http method in form.
Give each input in the form a name eg name="name" for name inputted.
Refactor app.py line 32 to specify get and post methods allowed.
Check debugger for a 200 response code when form clicked. (Everything works)
Import request library from Flask in app.py line 3
Use if request.method on app.py line 34 to print message and form data to debugger when form used.
Import flash function from flask (line 3 of app.py)
Add flashed message to contact view in app.py
Add with block to contact.html to display flash message

### Resources and reference / support used
VSCode setup Instructions:
https://code.visualstudio.com/docs/python/tutorial-flask

Bootstrap template from:
https://startbootstrap.com/themes/clean-blog/

Text content from:
https://lotr.fandom.com/wiki/Thorin_and_Company