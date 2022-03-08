import unittest

from importlib_metadata import email
from app.models import User

class UserTest(unittest.TestCase):
    def setUp(self):
        self.new_user = User(username = 'melo',password ='1234',email='melo@gmail.com')

    def tearDown(self):
        User.query.delete()

    def test_check_instance_var(self):
        self.assertEquals(self.new_user.username,'melo')

    def test_save_user(self):

        self.new_user.save_user()
        self.assertTrue(len(User.query.all())>0)

