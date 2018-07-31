from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
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
        # self.assertTrue(response.content.strip().startswith(b'<html>'))
        # self.assertIn(b'<title>To-Do lists</title>', response.content.strip())
        # self.assertTrue(response.content.strip().endswith(b'</html>'))
        expect_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expect_html)
