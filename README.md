
# ~finance101~ POCKET SENSE

# Requirements
- Python 3.6.9
- Flask 1.1.2
- Werkzeug 1.0.1

# Install [Flask](https://flask.palletsprojects.com/en/1.1.x/installation/)

**Mac or Linux**
- fork repo (https://github.com/QuaranTEAM-code/finance101)
- git clone https://github.com/{username}/finance101
- cd finance101
- python3 -m venv venv 
- . venv/bin/activate
- sudo pip3 install Flask
- export FLASK_APP=fin
- export FLASK_ENV=development
- flask initdb
- flask run

**Windows**

  fork repo (https://github.com/QuaranTEAM-code/finance101)
- cmd ( cd Dekstop)
- git clone https://github.com/{username}/finance101
-  py -3 -m venv venv (creating an V.Env && only created one Time)(**First Time**)
- venv\Scripts\activate
- pip3 install flask
- set FLASK_APP=fin
- set FLASK_ENV=development
-  *before running our application .. initiate the database*
- flask initdb (empty db)
- flask run 
- open  http://127.0.0.1:5000/home



# Update (First Time)
- git remote -v
- git remote add upstream https://github.com/QuaranTEAM-code/finance101 (single time)
- git fetch upstream
- git checkout master
- git merge upstream/master

------
- git pull (**After above steps .. use git pull to update each time**)




# Contribute
- git add {new code added in file .file_name}
- git commit -m "New Feature Added"
- git push
- create a pull request





