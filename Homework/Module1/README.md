# Homework 1
### Question 1. Install Django
`Yes`
``` [Bash]
pip install django
python -m django --version
```
`5.2.8`
### Question 2. Project and App
`manage.py`
```
django-admin startproject djproject1
cd djproject1
python manage.py startapp djapp1
```
### Question 3. Django models
`Add the models to the admin panel`
Models are used to define data models to interact with database. Register models in the `admin.py`. None of the other answers really addressed data or databases.
### Question 4. TODO Logic
`views.py`
Contains the functions and/or classes.
### Question 5. Templates
`TEMPLATES['DIRS'] in project's settings.py`
Search for template files in the `DIRS`.
### Question 6. Tests
`python manage.py test`
Runs the tests that have been created.
