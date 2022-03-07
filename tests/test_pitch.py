from importlib_metadata import email
from app.models import Comment, Pitch,User
from app import db

def setUp(self):
    self.new_User = User(username = 'Melo',password='1234',email = 'melo@gmail.com')
    self.new_pitch = Pitch()
    self.new_comment = Comment()

def tearDown(self):
    Pitch.query.delete()
    User.query.delete()

def test_check_instance_variable(self):
    self.assertEquals(self.new_review.pitch_category,'Religion')
    self.asserEquals(self.new_pitch.content,'religion dont define who your are')

def test_save_pitch(self):
    self.new_pitch.save_pitch()
    self.assertTrue(len(Pitch.query.all())>0)
