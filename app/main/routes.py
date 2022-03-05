
from flask import render_template
from flask_login import login_required
from app.models import Pitch
from . import main


@main.route('/')
def index():
    motivation_pitch = Pitch.get_pitches('motivation')
    promotion_pitch = Pitch.get_pitches('promotion')
    technology_pitch = Pitch.get_pitches('technology')
    religion_pitch = Pitch.get_pitches('religion')

    title = 'Home - One Minute Pitch'
    return render_template('index.html',title=title, motivation=motivation_pitch,promotion=promotion_pitch,technology=technology_pitch,religion=religion_pitch)
   

