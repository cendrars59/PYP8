from django.test import SimpleTestCase
from django.urls import resolve, reverse

from pages.views import home, mentions


class TestUrls(SimpleTestCase):

    # Checking URL homepage is resolved
    def test_homepage_url_is_resolved(self):
        url = reverse('pages-home')
        self.assertEquals(resolve(url).func, home)

    # Checking URL mentions is resolved
    def test_mentions_url_is_resolved(self):
        url = reverse('pages-mentions')
        self.assertEquals(resolve(url).func, mentions)
