from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.test import TestCase
from .views import home_page

# Create your tests here.


# class SmokeTest(TestCase):
#
#     def test_bad_maths(self):
#         self.assertEqual(1+1, 3)


class HomePageTest(TestCase):

    def test_root_url_resolves_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_return_corrent_html(self):
        request = HttpRequest()
        response = home_page(request)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>To-Do</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))
