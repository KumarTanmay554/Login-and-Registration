from flask import Flask,render_template , url_for, redirect, session
from flask_login import UserMixin
from functools import wraps
import pymongo

app = Flask(__name__)
app.secret_key = 'thisisthesecretkeyformyfuckingwebsite'

#database
client = pymongo.MongoClient('localhost', 27017)
db = client.user_login_system

#decorators
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect('/')
        
    return wrap
app = Flask(__name__)

#Routes
from user import routes


@app.route('/')
def home():
    return render_template('hom.html')

@app.route('/dashboard/')
def dashboard():
    return render_template('index2.html')

# @app.route('/register')
# def register(): 
#     return render_template('res.html')

# if __name__ == '__main__':
#     app.run(debug=True)