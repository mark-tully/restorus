from django.test import TestCase
from django.test.client import Client

from dictionary.models import Definition


class TestDefinitionModel(TestCase):

    def _create_definition(self):
        definition = Definition.objects.create(title='Test Definition', body='Test body')
        definition.save()
        return definition

    def test_successful_vars(self):
        definition = self._create_definition()
        self.assertEquals(definition.title, 'Test Definition')
        self.assertEquals(definition.body, 'Test body')
        self.assertEquals(definition.slug, 'test-definition')
        self.assertFalse(definition.sticky)
        self.assertEquals(definition.__str__(), 'Test Definition, Test body')

    def test_failing_vars(self):
        definition = self._create_definition()
        self.assertNotEquals(definition.title, 'Test body')


class TestDictionaryView(TestCase):

    def setUp(self):
        self.client = Client()

    def test_successful_vars(self):
        response = self.client.get('/dictionary/')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.context['title'], 'Political Dictionary')

    def test_failing_vars(self):
        response = self.client.get('/dictionary/')
        self.assertNotEquals(response.status_code, 404)
        self.assertNotEquals(response.context['title'], 'Other')


class TestDefinitionView(TestCase):

    def _create_definition(self):
        definition = Definition.objects.create(title='Test Definition', body='Test body')
        definition.save()
        return definition

    def setUp(self):
        self._create_definition()
        self.client = Client()

    def test_successful_vars(self):
        response = self.client.get('/define/test-definition/')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.context['title'], 'Define Test Definition')

    def test_failing_vars(self):
        response = self.client.get('/define/test-definition/')
        self.assertNotEquals(response.status_code, 404)
        self.assertNotEquals(response.context['title'], 'Other')
