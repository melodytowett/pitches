from crypt import methods
from turtle import title
from flask import redirect, render_template,redirect,url_for
from importlib_metadata import email

from app import auth

from..models import User
from.forms import RegistrationForm
from..import db


@auth.route('/reqister',methods['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.emali.data,username=form.username.data,password = form.password.data )
        
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
        title = 'New Account'

    return render_template('auth/resgister.htm', registration_form = form)



