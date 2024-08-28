from crypt import methods

from app import app
from app.forms import Loginform
from flask import render_template

@app.route('/')
@app.route('/home')
def home():
    user1 ={'username': 'Ayesha', 'password': 'meow'}
    return render_template('home.html', title='Train2Train', user=user1)

@app.route('/login', methods= ["GET", "POST"])
def login():
    form = Loginform()
    return render_template('login.html', title= 'Log in', form=form)