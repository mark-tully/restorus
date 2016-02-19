import os
import time
import datetime
from urllib.parse import urlparse

from django.core.management import BaseCommand
from django.contrib.auth.models import User
from django.contrib.redirects.models import Redirect
from django.contrib.sites.models import Site

from bs4 import BeautifulSoup

from articles.models import Topic, Article


class Command(BaseCommand):
    help = 'imports the old wordpress content into the shiny django app'

    def handle(self, *args, **kwargs):
        xml_file = os.path.join(os.path.dirname(__file__), 'restorus.xml')
        xml = open(xml_file, 'r').read()
        soup = BeautifulSoup(xml, 'xml')
        items = soup.find_all('item')  # find all blog posts.

        topics = [u'Politics', u'Religion', u'Culture', u'Arts', u'Tradition', u'Customs', u'Science',
                  u'Economics', u'Jurisprudence', u'Climate', u'Philosophy']

        for topic in topics:
            t = Topic.objects.get_or_create(title=topic)

        for item in items:
            author = User.objects.get(username='mark')
            time_string = item.post_date.string
            time_obj = time.strptime(time_string, "%Y-%m-%d %H:%M:%S")
            time_epoch = time.mktime(time_obj)
            date = datetime.datetime.fromtimestamp(time_epoch)
            if item.category.string == 'carl schmitt':
                category = 'Politics'
            elif item.category.string == 'occupy wall street':
                category = 'Politics'
            elif item.category.string == 'fascism':
                category = 'Politics'
            elif item.category.string == 'liberalism':
                category = 'Politics'
            elif item.category.string == 'internationalism':
                category = 'Politics'
            else:
                category = item.category.string
            category = Topic.objects.get(title=category)
            body = item.encoded.string
            if body.startswith('[caption'):
                loc = body.find('[/caption]')
                loc = loc + 10
                body = body[loc:]
            old_full_path = urlparse(item.link.text)
            old_path = old_full_path.path
            article = Article.objects.create(
                title=item.title.string,
                body=body,
                date=date,
                author=author,
                topic=category
            )
            article.save()
            site = Site.objects.get(id=1)
            redirect = Redirect.objects.create(
                site=site,
                old_path=old_path,
                new_path=article.get_absolute_url()
            )
            redirect.save()

            # %Y-%m-%d %H:%M:%S
