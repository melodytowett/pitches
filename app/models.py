
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, current_user
from.import login_manager
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Pitch:
    all_pitches = []

    def __init__(self,id,title,category,content):
        self.id = id
        self.title=title
        self.category = category
        self.content = content

    def save_pitch(self):
        Pitch.all_reviews.append(self)

    @classmethod
    def get_pitches(cls,id):
        response=[]
        for pitch in cls.all_pitvhes:
            if pitch.pitche_id ==id:
                response.append(pitch)
        return response


class User(UserMixin,db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    password_hash = db.Column(db.String(255))
    pass_secure  = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    # role_id= db.Column(db.Integer,db.ForeignKey('pitches.id'))
    pitches = db.relationship('Pitch',backref = 'user',lazy = "dynamic")

    def save(self):
        db.session.add(self)
        db.session.commit()

    '''
    decorator to create a write only class property password
    '''
    @property
    def password(self):
        raise AttributeError('Password attribute cannot be read')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)
    

    def __repr__(self):
        return f'User {self.username}'

class Pitch(db.Model):
    __tablename__ ="pitches"
    id = db.Column(db.Integer, primary_key=True)
    pitch_title = db.Column(db.String)
    content = db.Column(db.Text())
    time_posted = db.Column(db.DateTime,default=datetime.utcnow)
    category = db.Column(db.String,nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    comment = db.relationship('Comment',backref = 'pitch',lazy = "dynamic")
    upvote = db.relationship('Upvote',backref = 'pitch',lazy ="dynamic")
    downvote = db.relationship('Downvote',backref ='pitch',lazy ="dynamic")


    '''
    Method to save pitch to session and commit is to database
    '''

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    # def __repr__(self):
    #     return f'pitch{self.c}'
    '''
    classmethod that will take in pitch id and retrive them
    '''

class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer,primary_key = True)
    comment  = db.Column(db.Text())
    pitch_id = db.Column(db.Integer,db.ForeignKey("pitches.id"))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

  
    def __repr__(self):
        return f'User {self.username}'

class Upvote(db.Model):
    __tablename__ = 'upvotes'
    id = db.Column(db.Integer,primary_key=True)
    upvote = db.Column(db.Integer,default=1)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id')) 

    def save(self):
        db.session.add(self)
        db.session.commit()

    def upvote(cls,id):
        upvote_pitch = Upvote(user=current_user, pitch_id=id)
        upvote_pitch.save()

    @classmethod
    def all_upvotes(cls):
        upvotes = Upvote.query.filter_by(pitch_id=id).all()
        return upvotes

    def __repr__(self):
        return f'User{self.username}'
class Downvote(db.Model):
    __tablename__ = 'downvotes'
    id = db.Column(db.Integer,primary_key=True)
    downvote = db.Column(db.Integer,default=1)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    pitch_is = db.Column(db.Integer,db.ForeignKey("pitches.id"))

    def save(self):
        db.session.add(self)
        db.session.commit()
    



    def __repr__(self):
        return f'User{self.username}'

