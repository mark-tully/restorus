from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
import django.views

import core.views
import dictionary.views
import articles.views
import search.views

admin.autodiscover()



urlpatterns = [
                       url(r'^$', core.views.index_page, name='index_page'),

                       # dictionary

                       url(r'^dictionary/$', dictionary.views.dictionary_view, name='dictionary_view'),
                       url(r'^define/(?P<slug>[a-z0-9_-]+)/$', dictionary.views.definition_view,
                           name='definition_view'),

                       # studies
                       url(r'^studies/$', articles.views.studies_view, name='studies_view'),
                       url(r'^study/(?P<slug>[a-z0-9_-]+)/$', articles.views.study_page, name='study_page'),

                       # articles

                       url(r'^articles/(?P<topic>[a-z0-9_-]+)/(?P<slug>[a-z0-9_-]+)/$', articles.views.article_page,
                           name='article_page'),
                       url(r'^articles/(?P<topic_slug>[a-z0-9_-]+)/$', articles.views.topic_view, name='topic_view'),
                       url(r'^tag/(?P<slug>[a-z0-9_-]+)/$', articles.views.tag_view),

                       # reviews

                       url(r'^reviews/$', articles.views.reviews_view, name='reviews_view'),
                       url(r'^reviews/(?P<slug>[a-z0-9_-]+)/$', articles.views.review_page, name='review_page'),

                       # search

                       url(r'^search/', search.views.search_page, name='search_page'),

                       # sites of interest

                       url(r'^sites-of-interest/$', core.views.links_page, name='links_page'),

                       # blog
                       url(r'^blog/$', core.views.blog_view, name='blog_view'),
                       url(r'^blog/(?P<slug>[a-z0-9_-]+)/$', core.views.blog_post, name='blog_post'),


                       url(r'^admin/', include(admin.site.urls)),
                       ]
