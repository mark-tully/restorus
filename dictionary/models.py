from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.text import slugify


@python_2_unicode_compatible
class Definition(models.Model):
    title = models.CharField(max_length=125)
    date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    sticky = models.BooleanField(default=False)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return '%s, %s' % (self.title, self.body)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Definition, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return '/define/%s/' % (self.slug,)