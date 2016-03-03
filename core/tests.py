from django.test import TestCase
from django.test.client import Client

from core.models import BlogPost, Link


class TestBlogModel(TestCase):

    def _create_blog_post(self):
        post = BlogPost.objects.create(title='Blog Post', description='Test description', body='Stuff')
        post.save()
        return post

    def test_correct_vars(self):
        post = self._create_blog_post()
        self.assertEquals(post.title, 'Blog Post')
        self.assertEquals(post.slug, 'blog-post')
        self.assertEquals(post.description, 'Test description')
        self.assertEquals(post.body, 'Stuff')
        self.assertEquals(post.__str__(), 'Blog Post, Test description, Stuff')

    def test_failing_vars(self):
        post = self._create_blog_post()
        self.assertNotEquals(post.title, 'Other')


class TestLinkModel(TestCase):

    def _create_link(self):
        link = Link.objects.create(title='Restorus', url='http://restorus.org')
        link.save()
        return link

    def test_successful_vars(self):
        link = self._create_link()
        self.assertEquals(link.title, 'Restorus')
        self.assertEquals(link.url, 'http://restorus.org')
        self.assertEquals(link.__str__(), 'Restorus')

    def test_failing_vars(self):
        link = self._create_link()
        self.assertNotEquals(link.title, 'Other')


class TestIndexView(TestCase):

    def setUp(self):
        self.client = Client()

    def test_successful_vars(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.context['title'], 'Conservative Blog & News')

    def test_failing_vars(self):
        response = self.client.get('/')
        self.assertNotEquals(response.status_code, 500)
        self.assertNotEquals(response.context['title'], 'Something Else')

    def test_pagination(self):
        response = self.client.get('/?page=57')
        self.assertEquals(response.status_code, 200)


class TestLinksView(TestCase):

    def setUp(self):
        self.client = Client()

    def test_successful_vars(self):
        response = self.client.get('/sites-of-interest/')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.context['title'], 'Sites of Interest')

    def test_failing_vars(self):
        response = self.client.get('/sites-of-interest/')
        self.assertNotEquals(response.status_code, 404)
        self.assertNotEquals(response.context['title'], 'Something Else')


class TestBlogView(TestCase):

    def setUp(self):
        self.client = Client()

    def test_successful_vars(self):
        response = self.client.get('/blog/')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.context['title'], 'Making Restorus')

    def test_failing_vars(self):
        response = self.client.get('/blog/')
        self.assertNotEquals(response.status_code, 404)
        self.assertNotEquals(response.context['title'], 'Something Else')

    def test_pagination(self):
        response = self.client.get('/blog/?page=57')
        self.assertEquals(response.status_code, 200)


class TestBlogPostView(TestCase):

    def _create_blog_post(self):
        post = BlogPost.objects.create(title='Blog Post', description='Test description', body='Stuff')
        post.save()
        return post

    def setUp(self):
        self.post = self._create_blog_post()
        self.client = Client()

    def test_successful_vars(self):
        response = self.client.get('/blog/blog-post/')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.context['title'], 'Blog Post')

    def test_failing_vars(self):
        response = self.client.get('/blog/blog-post/')
        self.assertNotEquals(response.status_code, 404)
        self.assertNotEquals(response.context['title'], 'Other')
