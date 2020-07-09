from django.test import TestCase

from catlog.models import User


class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        User.objects.create(
            username='dummy_user_name',
            email='Dummy@email.com',
            password1='dummy_pwd_1',
            password2='dummy_pwd_1',
        )

    def test_username(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('username').verbose_name
        self.assertEquals(field_label, 'username')

    def test_email(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('email').verbose_name
        self.assertEquals(field_label, 'email')

    def test_pwd1(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('password1').verbose_name
        self.assertEquals(field_label, 'password1')

    def test_pwd2(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('password2').verbose_name
        self.assertEquals(field_label, 'password2')
