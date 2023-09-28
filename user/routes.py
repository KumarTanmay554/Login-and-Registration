from flask import Flask
from app import app
from user.models import Person

# For Signing Up
@app.route('/person/signup/', methods=['POST'])
def signup():
    return Person().signup()

# For Signing Out
@app.route('/person/signout')
def signout():
  return Person().signout()

# For Login
@app.route('/person/login', methods=['POST'])
def login():
  return Person().login()