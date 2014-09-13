import os
import time
import datetime

from django.core.management import BaseCommand
from django.contrib.auth.models import User
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
                  u'Economics', u'Jurisprudence', u'Climate']

        for topic in topics:
            t = Topic.objects.get_or_create(title=topic)

        for item in items:
            author = User.objects.get(username='mark')
            time_string = item.post_date.string
            time_obj = time.strptime(time_string, "%Y-%m-%d %H:%M:%S")
            time_epoch = time.mktime(time_obj)
            date = datetime.datetime.fromtimestamp(time_epoch)
            article = Article.objects.create(
                title=unicode(item.title.string),
                body=unicode(item.encoded.string),
                date=date,
                author=author,
            )
            article.save()

            # %Y-%m-%d %H:%M:%S