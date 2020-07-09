from django.test import TestCase
from django.urls import resolve, reverse

from catlog.views import search


class TestUrls(TestCase):

    # Checking URL homepage is resolved
    def test_search_url_is_resolved(self):
        response = self.client.get(reverse('search'))
        self.assertEquals(response.satus_code, 200)
