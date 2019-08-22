# Python with Flask Introduction

## NB Project created following tutorial followed from the Code Institute.
Adapted to use VSCode on a mac instead of AWS Cloud9 as used in the tutorial.
## This readme file is the developers own documentation for the learning project.

## View deployed project here: https://thorin-and-company-learning.herokuapp.com/

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

## Features
* Responsive bootstrap template
* Consistent header across all pages
* Hero image on home page
* Consistent header styles throughout via bootstrap template
* About page features bio information on each member
* About page loads data from ad hoc json database and links to sub pages for each element in the database
* Contact form with logging of content submitted and flash message in response

## Technologies
* HTML
* CSS
* Bootstrap
* Python
* Flask
* Jinja

## Future Plans
* Read Jinja and Flask documentation fully, follow Flask demo tutorial
* Fully functioning email form by adding a flask Extension
* Create a branch, load json data from Star Wars API and use this as the source for a Star Wars character profile
* Create a branch and refactor the project for a Hogwarts Students database, including a database for each of the four houses

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

### Deployment
#### Four steps to deploying in Heroku
1. Create Heroku app
2. Link git repo
3. Create requirements.txt
4. Create Procfile

Type **heroku** to check Heroku installed.
If not installed, install heroku with **brew tap heroku/brew && brew install heroku**
Use **heroku login** to login from CLI. (Opens browser)
Use **heroku apps** to list apps created
Can use **heroku apps:rename newnamehere --app currentnamehere** to rename
Check app is running eg **https://thorin-and-company-learning.herokuapp.com/**
Link github repo to Heroku
Use **git remote -v** to check remote link - should be absent
Go to Heroku Settings page for this project 
Copy git url for this project eg: https://git.heroku.com/thorin-and-company-learning.git
In CLI used **git remote add heroku https://git.heroku.com/thorin-and-company-learning.git** or equivalent
Use **git remote -v** to check above
Use **git status** to check status is clean
Use **git push -u heroku master** to push files
Error: no default language detected.

#### Create requirements.txt
Type **sudo pip3 freeze --local > requirements.txt** to create requirements.txt file in current directory
Check requirements.txt exists and has content expected eg Flask
Pip will install python and requirements.

#### Create proc file to instruct Heroku how to run project
The proc file is a Heroku specific file that tells Heroku how to run project
Use **echo web: python app.py > Procfile** to redirect to Procfile
Use **git add Procfile** to add Procfile and commit. NB Use capital p
Use **git push** to push files
Still will not run on Heroku - need to start web process.
Use **heroku ps:scale web=1** to start web process
Set IP and Port environment variables on Heroku project settings.
Set Config vars to: IP 0.0.0.0 and PORT to 5000
Click **More <>** button **Restart all dynos** in Heroku
App should now be running fully in the browser.

#### Troubleshooting
Need to replace:

if __name__ == "__main__": 
    app.run(debug=True) 
with
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)

In app.py

By using the IP and PORT environment variables in your code you can keep the same code for all computers and then set the values locally in config vars or in a bash script. 

### Resources and reference / support used
VSCode setup Instructions:
https://code.visualstudio.com/docs/python/tutorial-flask

Bootstrap template from:
https://startbootstrap.com/themes/clean-blog/

Text content from:
https://lotr.fandom.com/wiki/Thorin_and_Company

Installing Heroku:
https://devcenter.heroku.com/articles/heroku-cli

Jinja documentation:
https://jinja.palletsprojects.com/en/2.10.x/

Flask documentation:
https://flask.palletsprojects.com/en/1.0.x/

Using python environments in VScode:
https://code.visualstudio.com/docs/python/environments

