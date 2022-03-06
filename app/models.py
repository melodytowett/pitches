from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from.import login_manager
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'
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
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    # comment = db.relationship('Comment',backref = 'pitch',lazy = "dynamic")
    upvote = db.Column(db.String)
    downvote = db.Column(db.String)


    '''
    Method to save pitch to session and commit is to database
    '''

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    '''
    classmethod that will take in pitch id and retrive them
    '''

    @classmethod
    def get_pitches(cls,id):
        pitches = Pitch.query.filter_by(pitch_id = id).all()
        return pitches

    def __repr__(self):
        return f'User {self.username}'
    
