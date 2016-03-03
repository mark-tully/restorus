from django.test import TestCase
from django.test.client import Client


class TestSearchView(TestCase):

    def setUp(self):
        self.client = Client()

    def test_basic_search_page(self):
        response = self.client.get('/search/')
        self.assertEquals(response.status_code, 200)

    def test_provided_search(self):
        response = self.client.get('/search/?q=moldbug')
        self.assertEquals(response.status_code, 200)
