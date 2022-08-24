from django.test import SimpleTestCase
from django.contrib.auth.models import User

class TestSignUp(SimpleTestCase):
    
    def create_user(self):
        user = User.objects.create_user(username='username', email='auto_test@gmail.com')
        user.set_password('password123')
        user.save()
        self.assertEqual(str(user), 'auto_test@gmail.com')
