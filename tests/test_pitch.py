from app.models import Pitch,User
from app import db
import unittest

class PitchTest(unittest.TestCase):
    '''
    Creating n instance of User and pitch and pass it
    '''
    def setUp(self):
        self.user_Melo = User(username = 'melo',password='1234',email = 'melo@gmail.com')
        self.new_pitch = Pitch(category="Promotion", content='cool promotion',user = self.user_Melo)

    def tearDown(self):
        Pitch.query.delete()
        User.query.delete()

    def test_check_instance_variable(self):
        self.assertEquals(self.new_pitch.category,'Promotion')
        self.assertEquals(self.new_pitch.content,'cool promotion')
        self.assertEquals(self.new_pitch.user,self.user_Melo)

    def test_save_pitch(self):
        self.new_pitch.save_pitch()
        self.assertTrue(len(Pitch.query.all())>0)
