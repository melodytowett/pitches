from importlib.resources import contents
from xml.etree.ElementTree import Comment
from flask import redirect, render_template, request, url_for,abort
from flask_login import current_user, login_required
from app.main.forms import PitchForm,UpdateProfile,CommentForm
from app.models import Pitch, User
from . import main
from ..import db,photos


@main.route('/')
def index():
   
    pitches = Pitch.query.all()
    motivation_pitch = Pitch.query.filter_by( category ='motivation').all()
    promotion_pitch = Pitch.query.filter_by(category = 'promotion').all()
    technology_pitch = Pitch.query.filter_by(category='technology').all()
    religion_pitch = Pitch.query.filter_by(category='religion').all()

    title = 'Home - One Minute Pitch'
    return render_template('index.html',title=title, pitches=pitches,motivation=motivation_pitch,promotion=promotion_pitch,technology=technology_pitch,religion=religion_pitch)

@main.route('/pitch/content/new<int:id>',methods = ['GET',"POST"])
@login_required
def create_pitch(id):
   form = PitchForm()
#    Pitch = get_pitches(id)
   if form.validate_on_submit():
       title = form.title.data
       Pitch = form.content.data
       category = form.category.data
       new_pitch = Pitch(title = title, pitch_id=Pitch,category = category,user = current_user)
       new_pitch.save_pitch()
       return redirect(url_for('main.index' ))

   return render_template('pitches.html', form=form)


@main.route('/comment/<int:pitch_id>', methods=['POST','GET'])
@login_required
def comment(pitch_id):
    form = CommentForm()
    pitch = Pitch.query.get(pitch_id)
    comment = Comment.query.filter_by(pitch_id = pitch_id).all()
    if form.validate_on_submit():
        comment = form.Comment.data
        pitch_id = pitch_id
        new_comment = Comment(comment = comment,pitch_id = pitch,user = current_user)
        new_comment.save_coment()
        return redirect(url_for('.comment',pitch_id = pitch_id))

    return render_template('comment.html', form = form,pitch = pitch,comment = comment)


@main.route('/user/<uname>')
@login_required
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    content = Pitch.query.filter_by(user = current_user).all()
    if user is None:
        abort(404)

    return render_template("profile/profile.html",user = user,content = content) 

@main.route('/user/<uname>/update/pic', methods =['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_patch =path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))


@main.route('/user/<uname>/update')
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)
    form = UpdateProfile()
    
    if form.validate_on_submit():
        user.bio(form.bio.data)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template("profile/profile.html", form = form)
