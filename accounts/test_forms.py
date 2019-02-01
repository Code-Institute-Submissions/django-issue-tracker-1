from django.test import TestCase
from .forms import UserLoginForm
from .forms import UserRegistrationForm

# Create your tests here.
class TestUserLoginForm(TestCase):

    def test_cannot_create_an_account_with_just_a_name(self):
        form = UserLoginForm({'name': 'Create Tests'})
        self.assertFalse(form.is_valid())
        
        
    def test_correct_message_for_missing_name_in_login(self):
        form = UserLoginForm({'form': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['username'], [u'This field is required.'])
        self.assertEqual(form.errors['password'], [u'This field is required.'])
    
    def test_correct_message_for_missing_name(self):
        form = UserRegistrationForm({'form': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password2'], [u'This field is required.'])
        self.assertEqual(form.errors['password1'], [u'This field is required.'])
        