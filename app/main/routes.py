
from crypt import methods
from tkinter.tix import Form
from turtle import title
from unicodedata import category
from flask import redirect, render_template, url_for
from flask_login import current_user, login_required
from app.main.forms import Pitchform
from app.models import Pitch
from . import main


@main.route('/')
def index():
    motivation_pitch = Pitch.get_pitches('motivation').all()
    promotion_pitch = Pitch.get_pitches('promotion').all()
    technology_pitch = Pitch.get_pitches('technology').all()
    religion_pitch = Pitch.get_pitches('religion').all()

    title = 'Home - One Minute Pitch'
    return render_template('index.html',title=title, motivation=motivation_pitch,promotion=promotion_pitch,technology=technology_pitch,religion=religion_pitch)

@main.route('/pitch/new/<int:id>',methods = ['GET',"POST"])
@login_required
def create_pitch(id):
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


