from crypt import methods
from importlib.resources import contents
from flask import redirect, render_template, request, url_for,abort
from flask_login import current_user, login_required
from app.main.forms import PitchForm,UpdateProfile,CommentForm
from ..models import Pitch, User,Comment
from . import main
from ..import db,photos


@main.route('/',methods = ['GET','POST'])
def index():
    '''
    '''
    pitch=Pitch.query.all()
    motivation = Pitch.query.filter_by( category ='motivation').all()
    promotion = Pitch.query.filter_by(category = 'promotion').all()
    technology = Pitch.query.filter_by(category='technology').all()
    religion = Pitch.query.filter_by(category='religion').all()

    title = 'Home - One Minute Pitch'
    # return render_template('index.html',title=title)
    return render_template('index.html',pitch=pitch,motivation=motivation,promotion=promotion,technology=technology,religion=religion)


@main.route('/new_pitch',methods = ['GET',"POST"])
@login_required
def create_pitch():
   form = PitchForm()
#    Pitch = get_pitches(id)
   if form.validate_on_submit():
    #    title = form.title.data
       content = form.content.data
       category = form.category.data 

       new_pitch = Pitch( content=content,category = category,user = current_user)
       new_pitch.save_pitch()
       return redirect(url_for('main.index' ))

   return render_template('pitches.html', form=form)


@main.route('/comment/<int:pitch_id>', methods=['POST','GET'])
@login_required
def comment_sent(pitch_id):
    form = CommentForm()
    pitch = Pitch.query.get(pitch_id)
    # pitch = User.query.all()
    comment = Comment.query.filter_by(pitch_id = pitch_id).all()
    if form.validate_on_submit():
        comment = form.Comment.data
        pitch_id = pitch_id
        new_comment = Comment(comment = comment,pitch_id = pitch_id,user = current_user)
        new_comment.save_comment()
        return redirect(url_for('.comment',pitch_id = pitch_id))

    return render_template('comment.html', form = form, pitch= pitch,comment = comment)


@main.route('/user/<uname>/update')
@login_required
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    # content = Pitch.query.filter_by(user = current_user).all()
    if user is None:
        abort(404)

    return render_template("profile/profile.html",user = user) 


@main.route('/user/<uname>/update',methods = ['Get','POST'])
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

    return render_template("profile/update.html", form = form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))