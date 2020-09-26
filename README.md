
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


# Structure 
```
   .
  ├── fin
  │   ├── auth.py
  │   ├── db.py
  │   ├── __init__.py
  │   ├── schema.sql
  │   ├── static
  │   │   └── style.css
  │   ├── templates
  │   │   ├── auth
  │   │   │   ├── child_email_required.html
  │   │   │   ├── child_forget_passw.html
  │   │   │   ├── child_login.html
  │   │   │   ├── child_register.html
  │   │   │   ├── parent_login.html
  │   │   │   ├── parent_register.html
  │   │   │   └── update_child_passw.html
  │   │   ├── base.html
  │   │   ├── child_base.html
  │   │   ├── child_index.html
  │   │   ├── home.html
  │   │   ├── parent_index.html
  │   │   └── update_child_passw_base.html   
  ├── instance
  │   └── fin.sqlite
  ├── PocketSense1
  │   ├── css
  │   │   └── styles.css
  │   ├── index.html
  │   └── Login-Register
  │       ├── cRegister.html
  │       ├── css
  │       │   ├── main.css
  │       │   └── util.css
  │       ├── index.html
  │       ├── pLogin.html
  │       └── pRegister.html
  ├── Procfile
  ├── __pycache__
  │   └── secret.cpython-36.pyc
  ├── README.md
  ├── requirements.txt
  └── secret.py

  ```

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





