from django.shortcuts import render_to_response, RequestContext, get_object_or_404, render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.sitemaps import Sitemap

from core.models import Link, BlogPost
from articles.models import Article, Topic, Tag, Study, Review


def index_page(request):
    title = 'Conservative Blog & News'
    description = 'Restorus.org is a right wing conservative news blog aimed at providing commentary on classical and current issues.'
    articles_list = Article.objects.all().order_by('-date')
    paginator = Paginator(articles_list, 10)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    return render_to_response('index.html',
                              RequestContext(request,
                                             {'title': title, 'description': description,
                                              'articles': articles}))


def links_page(request):
    links = Link.objects.all()
    title = 'Sites of Interest'
    description = 'Interesting destinations around the web.'
    return render_to_response('links.html',
                              RequestContext(request,
                                             {'title': title, 'description': description,
                                              'links': links}))


def blog_view(request):
    title = 'Making Restorus'
    description = 'from right_wing import restorus'
    posts_list = BlogPost.objects.all().order_by('-date')
    paginator = Paginator(posts_list, 10)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render_to_response('blog/blog_view.html',
                              RequestContext(request,
                                             {'title': title, 'description': description,
                                              'posts': posts}))


def blog_post(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    title = post.title
    description = post.description
    return render_to_response('blog/blog_post.html',
                              RequestContext(request,
                                  {'title': title, 'description': description,
                                   'post': post}))


def robots_txt(request):
    return render(request, template_name='robots.txt', content_type='text/plain')


class ArticleSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.6

    def items(self):
        return Article.objects.all()


class TopicSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.9

    def items(self):
        return Topic.objects.all()


class TagSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.8

    def items(self):
        return Tag.objects.all()


class StudySitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.7

    def items(self):
        return Study.objects.all()


class ReviewSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.7

    def items(self):
        return Review.objects.all()
