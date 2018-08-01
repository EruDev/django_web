from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase
from .views import home_page
from .models import Item

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

    def test_home_page_can_save_a_POST_reuqest(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new list item'

        response = home_page(request)

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')

    def test_home_page_redirect_after_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new list item'

        response = home_page(request)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')

    def test_home_page_only_saves_items_when_necessary(self):
        request = HttpRequest()
        home_page(request)
        self.assertEqual(Item.objects.count(), 0)

    def test_home_page_display_all_items(self):
        Item.objects.create(text='itemy 1')
        Item.objects.create(text='itemy 2')

        request = HttpRequest()
        response = home_page(request)

        self.assertIn('itemy 1', response.content.decode())
        self.assertIn('itemy 2', response.content.decode())


class ItemModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()

        save_items = Item.objects.all()
        self.assertEqual(save_items.count(), 2)

        save_items_first = save_items[0]
        save_items_second = save_items[1]
        self.assertEqual(save_items_first.text, 'The first (ever) list item')
        self.assertEqual(save_items_second.text, 'Item the second')
