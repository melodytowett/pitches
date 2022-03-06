from crypt import methods
from turtle import title
from flask import redirect, render_template,redirect,url_for,flash,request
from importlib_metadata import email
from flask_login import login_user
from app import auth
from..models import User
from.forms import RegistrationForm,LoginForm
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

@auth.route('/login',methods=['GET','POST'])
def login():
    login_form =LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            return redirect(request.args.get('next')or url_for('main.index'))

        flash('Invald username or password')

    title = "Pitch Login"
    return render_template('auth/logi.html',login_form = login_form,title=title)




