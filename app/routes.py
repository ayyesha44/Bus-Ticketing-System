from app import app
from app.forms import Loginform
from flask import render_template, redirect, flash

@app.route('/login', methods= ["GET", "POST"])
def login():
    form = Loginform()
    if form.validate_on_submit():
        flash('Login requested for user {}, rememberme={}'.format(form.username.data, form.rememberme.data))
        return redirect('/index')
    return render_template('login.html', title= 'Log in', form=form)

