from crypt import methods
from flask import redirect, render_template, request, url_for,abort
from flask_login import current_user, login_required
from app.main.forms import PitchForm,UpdateProfile,CommentForm
from ..models import Pitch, Upvote, User,Comment,Downvote
from . import main
from ..import db,photos


@main.route('/',methods = ['GET','POST'])
def index():
    '''
    '''
    pitch=Pitch.query.all()
    title = 'Home - One Minute Pitch'
    return render_template('index.html',pitch=pitch, title=title)


@main.route('/new_pitch',methods = ['GET',"POST"])
@login_required
def create_pitch():
   form = PitchForm()
   if form.validate_on_submit():
       content = form.content.data
       category = form.category.data 
       new_pitch = Pitch( content=content,category = category,user = current_user)
       new_pitch.save_pitch()
   return render_template('pitches.html', form=form)


@main.route('/comment/new/<int:pitch_id>', methods=['POST','GET'])
@login_required
def comment_sent(pitch_id):
    form = CommentForm()
    comment = Comment.query.filter_by(pitch_id = pitch_id).all()
    if form.validate_on_submit():
        comment = form.Comment.data
        pitch_id = pitch_id
        new_comment = Comment(comment = comment,pitch_id = pitch_id,user = current_user)
        new_comment.save_comment()
    return render_template('comment.html', form = form,comment = comment)


@main.route('/user/<uname>/update')
@login_required
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    return render_template("profile/profile.html",user = user) 


@main.route('/user/<uname>/update',methods = ['GET','POST'])
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

@main.route('/like/<int:id>',methods=['GET','POST'])
@login_required
def upvote(id):
    pitches = Pitch.query.get(id)
    vote = Upvote(pitch=pitches,upvote=1)
    vote.save()
    return redirect(url_for('main.index',id=id))

@main.route('/dislike/<int:id>',methods=['GET','POST'])
@login_required
def downvote(id):
    pitches = Pitch.query.get(id)
    vote_not = Downvote(pitch=pitches,downvote=1)
    vote_not.save()
    return redirect(url_for('main.index'))


