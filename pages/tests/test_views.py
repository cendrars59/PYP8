from django.test import Client, TestCase
from django.urls import reverse


class TestViews(TestCase):
    def test_homepage_status(self):
        client = Client()
        response = client.get(reverse('pages-home'))
        self.assertEquals(response.status_code, 200)

    def test_homepage_template(self):
        client = Client()
        response = client.get(reverse('pages-home'))
        self.assertTemplateUsed(response, 'pages/home.html')

    def test_mentions_status(self):
        client = Client()
        response = client.get(reverse('pages-mentions'))
        self.assertEquals(response.status_code, 200)

    def test_mentions_template(self):
        client = Client()
        response = client.get(reverse('pages-mentions'))
        self.assertTemplateUsed(response, 'pages/mentions.html')

    # def test_redirection_to_mentions_from_home(self):
    #    client = Client()
    #    # First check for the default behavior
    #    response = self.client.get('/mentions/', follow=True)
    #    self.assertContains(response, 304)
