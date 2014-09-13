# global variables are dangerous things. you've been warned.
from django.conf import settings

from dictionary.models import Definition
from articles.models import Tag, Article
from search.forms import SearchForm


def site_name(request):
    return {
        'site_name': 'Conservative Blog & News',
    }


def MEDIA_URL(request):
    return {'MEDIA_URL': settings.MEDIA_ROOT}


def recent_definitions(request):
    recent = Definition.objects.all().order_by('-date')[:10]
    return {'recent_definitions': recent}


def sticky_definitions(request):
    sticky = Definition.objects.filter(sticky=True).all()
    return {'sticky_definitions': sticky}


def tags_list(request):
    tags = Tag.objects.all().order_by('-title')
    return {'tags_list': tags}


def sticky_articles(request):
    sticky = Article.objects.filter(sticky=True).all()


def search_form_processor(request):
    form = SearchForm()
    return {
        'search_form': form
    }