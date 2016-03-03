from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User

from articles.models import Tag, Topic, Article, Review, Study


class TestTagModel(TestCase):

    def setUp(self):
        pass

    def _create_tag(self):
        tag = Tag.objects.create(title='Test Tag')
        tag.save()
        return tag

    def test_correct_vars(self):
        tag = self._create_tag()
        self.assertEquals(tag.title, 'Test Tag')
        self.assertEquals(tag.slug, 'test-tag')
        self.assertEquals(tag.__str__(), 'Test Tag')
        self.assertEquals(tag.get_absolute_url(), '/tag/test-tag/')

    def test_failing_vars(self):
        tag = self._create_tag()
        self.assertNotEquals(tag.title, 'Something Else')
        self.assertNotEquals(tag.slug, 'something-else')
        self.assertNotEquals(tag.__str__(), 'Other')
        self.assertNotEquals(tag.get_absolute_url(), '/test-tag/')


class TestTopicModel(TestCase):

    def setUp(self):
        pass

    def _create_topic(self):
        topic = Topic.objects.create(title='Topic', intro='About the topic')
        topic.save()
        return topic

    def test_correct_vars(self):
        topic = self._create_topic()
        self.assertEquals(topic.title, 'Topic')
        self.assertEquals(topic.intro, 'About the topic')
        self.assertEquals(topic.slug, 'topic')
        self.assertEquals(topic.__str__(), 'Topic, About the topic')
        self.assertEquals(topic.get_absolute_url(), '/articles/topic/')

    def test_failing_vars(self):
        topic = self._create_topic()
        self.assertNotEquals(topic.title, 'Other')
        self.assertNotEquals(topic.intro, 'Other intro')
        self.assertNotEquals(topic.slug, 'Topic')
        self.assertNotEquals(topic.__str__(), 'Topic')
        self.assertNotEquals(topic.get_absolute_url(), '/topic/')


class ReviewModelTest(TestCase):

    def setUp(self):
        user = User.objects.create_user(username='mark', email='mark@example.com', password='password')
        user.save()
        self.user = user

    def _create_review(self):
        review = Review.objects.create(title='Review', description='What we review',
                                       author=self.user, teaser='Teaser', cta='http://restorus.org',
                                       body='Body')
        review.save()
        return review

    def test_successful_vars(self):
        review = self._create_review()
        self.assertEquals(review.title, 'Review')
        self.assertEquals(review.description, 'What we review')
        self.assertEquals(review.author.username, 'mark')
        self.assertEquals(review.teaser, 'Teaser')
        self.assertEquals(review.cta, 'http://restorus.org')
        self.assertEquals(review.slug, 'review')
        self.assertEquals(review.body, 'Body')
        self.assertEquals(review.__str__(), 'Review, What we review, Teaser, http://restorus.org, Body')
        self.assertEquals(review.get_absolute_url(), '/reviews/review/')

    def test_failing_vars(self):
        review = self._create_review()
        self.assertNotEquals(review.title, 'Other')
        self.assertNotEquals(review.description, 'Other')
        self.assertNotEquals(review.author.username, 'marktully')
        self.assertNotEquals(review.teaser, 'Other')
        self.assertNotEquals(review.cta, 'http://example.com')


class TestStudyModel(TestCase):

    def setUp(self):
        user = User.objects.create_user(username='mark', email='mark@example.com', password='password')
        user.save()
        self.user = user

    def _create_study(self):
        study = Study.objects.create(title='Study', description='Description', author=self.user,
                                     teaser='Teaser', body='Body')
        study.save()
        return study

    def test_correct_vars(self):
        study = self._create_study()
        self.assertEquals(study.title, 'Study')
        self.assertEquals(study.description, 'Description')
        self.assertEquals(study.author.username, 'mark')
        self.assertEquals(study.teaser, 'Teaser')
        self.assertEquals(study.body, 'Body')
        self.assertEquals(study.slug, 'study')
        self.assertFalse(study.sticky)
        self.assertEquals(study.__str__(), 'Study, Description, Teaser, Body')
        self.assertEquals(study.get_absolute_url(), '/study/study/')

    def test_failing_vars(self):
        study = self._create_study()
        self.assertNotEquals(study.title, 'Other')
        self.assertNotEquals(study.description, 'Other')
        self.assertNotEquals(study.author.email, 'mark@other.com')
        self.assertNotEquals(study.teaser, 'Other')
        self.assertNotEquals(study.body, 'Other')
        self.assertNotEquals(study.slug, 'other')
        self.assertNotEquals(study.get_absolute_url(), '/study/')


class ArticleModelTest(TestCase):

    def setUp(self):
        user = User.objects.create_user(username='mark', email='mark@example.com', password='password')
        user.save()
        topic = Topic.objects.create(title='Foobar', intro='About foobar')
        tag = Tag.objects.create(title='Tag')
        topic.save()
        tag.save()
        self.user = user
        self.tag = tag
        self.topic = topic

    def _create_article(self):
        article = Article.objects.create(title='Article Title', teaser='Teaser', author=self.user,
                                         topic=self.topic, body='Body')
        article.tags.add(self.tag)
        article.save()
        return article

    def test_successful_vars(self):
        article = self._create_article()
        self.assertEquals(article.title, 'Article Title')
        self.assertEquals(article.__str__(), 'Article Title, Teaser, Body')
        self.assertIn(self.tag, article.tags.all())
        self.assertEquals(article.topic.title, 'Foobar')
        self.assertEquals(article.get_absolute_url(), '/articles/foobar/article-title/')


class TestTopicView(TestCase):

    def _create_topic(self):
        topic = Topic.objects.create(title='Topic', intro='About the topic')
        topic.save()
        return topic

    def setUp(self):
        self.topic = self._create_topic()
        self.client = Client()

    def test_correct_view(self):
        response = self.client.get('/articles/topic/')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.context['title'], 'Topic Articles')
        self.assertEquals(response.context['description'], 'Read articles about Topic on Restorus.org')

    def test_pagination_view(self):
        response = self.client.get('/articles/topic/?page=57')
        self.assertEquals(response.status_code, 200)


class TestTagView(TestCase):

    def _create_tag(self):
        tag = Tag.objects.create(title='Test Tag')
        tag.save()
        return tag

    def setUp(self):
        self.tag = self._create_tag()
        self.client = Client()

    def test_correct_view(self):
        response = self.client.get('/tag/test-tag/')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.context['title'], 'Test Tag Articles')

    def test_pagination_view(self):
        response = self.client.get('/tag/test-tag/?page=57')
        self.assertEquals(response.status_code, 200)


class TestArticleView(TestCase):

    def setUp(self):
        user = User.objects.create_user(username='mark', email='mark@example.com', password='password')
        user.save()
        topic = Topic.objects.create(title='Foobar', intro='About foobar')
        tag = Tag.objects.create(title='Tag')
        topic.save()
        tag.save()
        self.user = user
        self.tag = tag
        self.topic = topic
        self.client = Client()

    def _create_article(self):
        article = Article.objects.create(title='Article Title', teaser='Teaser', author=self.user,
                                         topic=self.topic, body='Body')
        article.tags.add(self.tag)
        article.save()
        return article

    def test_successful_vars(self):
        self._create_article()
        response = self.client.get('/articles/foobar/article-title/')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.context['title'], 'Article Title')

    def test_failing_vars(self):
        self._create_article()
        response = self.client.get('/articles/foobar/article-title/')
        self.assertNotEquals(response.status_code, 404)
        self.assertNotEquals(response.context['title'], 'Other')


class TestReviewsPage(TestCase):

    def setUp(self):
        user = User.objects.create_user(username='mark', email='mark@example.com', password='password')
        user.save()
        self.user = user
        self.client = Client()

    def _create_review(self):
        review = Review.objects.create(title='Review', description='What we review',
                                       author=self.user, teaser='Teaser', cta='http://restorus.org',
                                       body='Body')
        review.save()
        return review

    def test_successful_vars(self):
        self._create_review()
        response = self.client.get('/reviews/review/')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.context['title'], 'Review')

    def test_failing_vars(self):
        self._create_review()
        response = self.client.get('/reviews/review/')
        self.assertNotEquals(response.status_code, 404)
        self.assertNotEquals(response.context['title'], 'Other')


class TestReviewIndexView(TestCase):

    def setUp(self):
        self.client = Client()

    def test_successful_vars(self):
        response = self.client.get('/reviews/')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.context['title'], 'Book & Product Reviews')

    def test_failing_vars(self):
        response = self.client.get('/reviews/')
        self.assertNotEquals(response.status_code, 404)
        self.assertNotEquals(response.context['title'], 'Other')

    def test_pagination(self):
        response = self.client.get('/reviews/?page=57')
        self.assertEquals(response.status_code, 200)


class TestStudyView(TestCase):

    def setUp(self):
        user = User.objects.create_user(username='mark', email='mark@example.com', password='password')
        user.save()
        self.user = user
        self.client = Client()

    def _create_study(self):
        study = Study.objects.create(title='Study', description='Description', author=self.user,
                                     teaser='Teaser', body='Body')
        study.save()
        return study

    def test_successful_vars(self):
        self._create_study()
        response = self.client.get('/study/study/')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.context['title'], 'Study')

    def test_failing_vars(self):
        self._create_study()
        response = self.client.get('/study/study/')
        self.assertNotEquals(response.status_code, 404)
        self.assertNotEquals(response.context['title'], 'Other')


class TestStudyIndexView(TestCase):

    def setUp(self):
        self.client = Client()

    def test_successful_vars(self):
        response = self.client.get('/studies/')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.context['title'], 'In-Depth Studies')

    def test_failing_vars(self):
        response = self.client.get('/studies/')
        self.assertNotEquals(response.status_code, 404)
        self.assertNotEquals(response.context['title'], 'Articles')

    def test_pagination(self):
        response = self.client.get('/studies/?page=57')
        self.assertEquals(response.status_code, 200)
