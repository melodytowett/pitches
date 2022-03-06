
from crypt import methods
from os import abort
from flask import redirect, render_template, url_for
from flask_login import current_user, login_required
from app.auth.pitch_view import login
from app.main.forms import Pitchform
from app.models import Pitch, User
from . import main


@main.route('/')
def index():
    
    pitches = Pitch.query.all()
    motivation_pitch = Pitch.query.filter_by('motivation').all()
    promotion_pitch = Pitch.query.filter_by('promotion').all()
    technology_pitch = Pitch.query.filter_by('technology').all()
    religion_pitch = Pitch.query.filter_by('religion').all()

    title = 'Home - One Minute Pitch'
    return render_template('index.html',title=title, motivation=motivation_pitch,promotion=promotion_pitch,technology=technology_pitch,religion=religion_pitch)

@main.route('/pitch_new>',methods = ['GET',"POST"])
@login_required
def create_pitch():
   form = Pitchform()
   #Pitch = get_pitches(id)
   if form.validate_on_submit():
       title = form.title.data
       content = form.content.data
       category = form.category.data

       new_pitch = Pitch(title = title, content=content,category = category,user = current_user)
       new_pitch.save_pitch()
       return redirect(url_for('main.index' ))

   return render_template('new_pitch.html', form=form)

# @main.route('/user/<uname>')
# @login_required
# def profile(uname):
#     user = User.query.filter_by(username = uname).first()
#     content = Pitch.query.filter_by(user = current_user).all()
#     if user is None:
#         abort(404)

#     return render_template("profile/profile.html",user = user,content = content) 


