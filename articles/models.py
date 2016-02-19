import datetime
import os

from django.db import models
from django.contrib.auth.models import User

from djorm_pgfulltext.models import SearchManager
from djorm_pgfulltext.fields import VectorField
from slugify import slugify


def article_upload_path_handler(instance, filename):
    return os.path.join('article_%s' % instance.slug, filename)


def study_upload_path_handler(instance, filename):
    return os.path.join('study_%s' % instance.slug, filename)


def review_upload_path_handler(instance, filename):
    return os.path.join('review_%s' % instance.slug, filename)


class Tag(models.Model):
    title = models.CharField(max_length=125, unique=True)
    slug = models.SlugField(max_length=125, blank=True)
    
    def __str__(self):
        return '%s' % (self.title,)
    
    def save(self, *args, **kwargs):
        if not self.id or self.slug:
            self.slug = slugify(self.title)
        super(Tag, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return '/tag/%s/' % (self.slug,)
        

class Topic(models.Model):
    title = models.CharField(max_length=75, unique=True)
    slug = models.SlugField(max_length=125, blank=True)
    intro = models.TextField(blank=True)
    
    def __str__(self):
        return '%s, %s' % (self.title, self.intro,)
    
    def save(self, *args, **kwargs):
        if not self.id or self.slug:
            self.slug = slugify(self.title, to_lower=True)
        super(Topic, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return '/articles/%s/' % (self.slug,)


class Article(models.Model):
    title = models.CharField(max_length=125)
    teaser = models.TextField(blank=True, null=True)
    author = models.ForeignKey(User)
    topic = models.ForeignKey(Topic, blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    date = models.DateTimeField(auto_now_add=False, editable=True, blank=True)
    body = models.TextField()
    image = models.ImageField(blank=True, null=True, upload_to=article_upload_path_handler)
    slug = models.SlugField(max_length=125, blank=True)
    search_index = VectorField()

    objects = SearchManager(
        fields=('title', 'teaser',),
        config = 'pg_catalog.english',
        search_field = 'search_index',
        auto_update_search_field = True
    )
    
    def __str__(self):
        return '%s, %s, %s' % (self.title, self.teaser, self.body,)
    
    def save(self, *args, **kwargs):
        if not self.id or self.slug:
            self.slug = slugify(self.title, to_lower=True)
        if not self.date:
            self.date = datetime.datetime.now()
        super(Article, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return '/articles/%s/%s/' % (self.topic.slug, self.slug)


class Review(models.Model):
    title = models.CharField(max_length=125)
    description = models.TextField()
    author = models.ForeignKey(User)
    teaser = models.TextField()
    image = models.ImageField(blank=True, null=True, upload_to=review_upload_path_handler)
    slug = models.SlugField(max_length=125, blank=True)
    cta = models.URLField(max_length=200)
    body = models.TextField()
    
    def __str__(self):
        return '%s, %s, %s, %s, %s' % (self.title, self.description, self.teaser,
                                       self.cta, self.body,)
    
    def save(self, *args, **kwargs):
        if not self.id or self.slug:
            self.slug = slugify(self.title, to_lower=True)
        super(Review, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return '/reviews/%s/' % (self.slug,)


class Study(models.Model):
    title = models.CharField(max_length=125)
    description = models.TextField()
    author = models.ForeignKey(User)
    teaser = models.TextField()
    image = models.ImageField(blank=True, null=True, upload_to=study_upload_path_handler)
    slug = models.SlugField(max_length=125, blank=True)
    body = models.TextField()
    sticky = models.BooleanField(default=False)

    def __str__(self):
        return '%s, %s, %s, %s' % (self.title, self.description, self.teaser,
                                   self.body,)

    def save(self, *args, **kwargs):
        if not self.id or self.slug:
            self.slug = slugify(self.title, to_lower=True)
        super(Study, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return '/study/%s/' % (self.slug,)
