from django.db import models

from slugify import slugify


class Link(models.Model):
    title = models.CharField(max_length=125)
    url = models.URLField(max_length=200)

    def __str__(self):
        return '%s' % (self.title,)


class BlogPost(models.Model):
    title = models.CharField(max_length=125)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)
    body = models.TextField()
    slug = models.SlugField(max_length=125, blank=True)

    def __str__(self):
        return '%s, %s, %s' % (self.title, self.description, self.body)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title, to_lower=True)
        super(BlogPost, self).save(*args, **kwargs)
