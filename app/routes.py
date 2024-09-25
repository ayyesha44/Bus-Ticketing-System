import sqlalchemy
from app.models import User
from app import app, db
from app.forms import Loginform, Signupform, Editprofileform
from flask import render_template, redirect, flash, request, url_for
from flask_login import current_user, login_user, login_required, logout_user
from app.models import User, Seat


@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('index.html', title="Home")

@app.route('/faq')
def faq():
    return render_template('faq.html', title="Frequently Asked Questions")

@app.route('/logout')
def logout():
    logout_user()
    return redirect('/index')

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
    return render_template('login.html', form=form, title="Login")

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
    return render_template('signup.html', form=form, title="Sign Up")

@app.route('/seats', methods=["GET", "POST"])
@login_required
def select_seat():
    seat = Seat.query.all()
    user = []
    i = 0
    if request.method =="POST":
        for x in range(1,36):
            tmp = request.form.get(str(x))
            if tmp == "1":
                seat_update = Seat.query.filter_by(id=str(x)).update(dict(selected=True))
                db.session.commit()
            elif tmp is None:
                tmp = "0"
            user += tmp


  
        return redirect(url_for("user", usr=user))
    else:
        return render_template("select_seat.html", seat=seat)

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"

@app.route('/booking')
@login_required
def booking():
    return render_template("booking.html")

@app.route('/profile')
@login_required
def profile():
    return render_template("profile.html")

@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = Editprofileform()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect('/edit_profile')
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    return render_template('edit_profile.html', title='Edit Profile', form=form)
