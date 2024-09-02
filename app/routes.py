import sqlalchemy
from app.models import User
from app import app, db
from app.forms import Loginform, Signupform
from flask import render_template, redirect, flash
from flask_login import current_user, login_user, login_required
from app.models import User

@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('index.html')

@app.route('/login', methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect('/index')
    form = Loginform()
    if form.validate_on_submit():
        user = db.session.scalar(sqlalchemy.select(User).where(User.username == form.username.data))
        if user is None or user.password != form.password.data:
            flash('Invalid username or password')
            return redirect('/login')
        login_user(user, remember=form.rememberme.data)
        return redirect('/index')
    return render_template('login.html', form=form)

@app.route('/signup', methods=["GET", "POST"])
def signup():
    form = Signupform()
    if form.validate_on_submit():
        user = db.session.scalar(sqlalchemy.select(User).where(User.username == form.username.data))
        if user is None:
            new_user = User(email=form.email.data, username=form.username.data, password=form.password.data)
            db.session.add(new_user)
            db.session.commit()
            flash(f'Registration successful for user {new_user.username}')
            return redirect('/login')
    return render_template('signup.html', form=form)
