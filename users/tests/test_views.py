from django.test import Client, TestCase
from django.urls import reverse


class TestViewsLogin(TestCase):
    def test_login_status(self):
        client = Client()
        response = client.get(reverse('login'))
        self.assertEquals(response.status_code, 200)

    def test_login_template(self):
        client = Client()
        response = client.get(reverse('login'))
        self.assertTemplateUsed(response, 'users/login.html')


class TestViewsRegister(TestCase):
    def test_register_status(self):
        client = Client()
        response = client.get(reverse('register'))
        self.assertEquals(response.status_code, 200)

    def test_register_template(self):
        client = Client()
        response = client.get(reverse('register'))
        self.assertTemplateUsed(response, 'users/register.html')


class TestViewsLogOut(TestCase):
    def test_logout_status(self):
        client = Client()
        response = client.get(reverse('logout'))
        self.assertEquals(response.status_code, 200)

    def test_register_template(self):
        client = Client()
        response = client.get(reverse('logout'))
        self.assertTemplateUsed(response, 'users/logout.html')
