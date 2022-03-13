import unittest
from app.models import User

class UserModelTest(unittest.TestCase):
    '''
    Test class to test user model
    '''
    def setUp(self):
        '''
        Setup function that instanciates user
        '''
        self.new_user = User(password = 'maembe')

    def test_password_setter(self):
        '''
        Function that tests password setter method
        '''
        self.assertTrue(self.new_user.password_hash is not None)

    def test_no_access_password(self):
        '''
        Function to confirm that the application raises an attribute error
        '''
        with self.assertRaises(AttributeError):
            self.new_user.password

    def test_password_verification(self):
        '''
        Function that access password property
        '''
        self.assertTrue(self.new_user.verify_password('maembe'))