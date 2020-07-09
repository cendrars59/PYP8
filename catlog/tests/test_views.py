from django.http import HttpRequest
from django.test import TestCase
from django.urls import resolve

from catlog.views import search


class SearchTest(TestCase):
    def test_root_url_resolves_to_search_view(self):
        found = resolve('/catalogue/search/')
        self.assertEqual(found.func, search)

    def test_search_page_returns_correct_html(self):
        request = HttpRequest()
        response = search(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<!DOCTYPE html>'))
        self.assertIn('<title>Search</title>', html)
        self.assertTrue(html.endswith('</html>'))
