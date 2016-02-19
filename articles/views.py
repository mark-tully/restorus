from django.shortcuts import render_to_response, RequestContext, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from articles.models import Topic, Tag, Article, Review, Study


def topic_view(request, topic_slug):
    topic = get_object_or_404(Topic, slug=topic_slug)
    articles_list = Article.objects.filter(topic=topic).order_by('-date')
    paginator = Paginator(articles_list, 10)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    title = '%s Articles' % (topic.title,)
    description = 'Read articles about %s on Restorus.org' % (topic.title,)
    return render_to_response('articles/topic_view.html',
                              RequestContext(request, {'title': title, 'description': description,
                                                       'articles': articles}))


def tag_view(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    articles_list = Article.objects.filter(tags=tag)
    paginator = Paginator(articles_list, 10)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    title = '%s Articles' % (tag.title,)
    description = 'Read about %s and more at Restorus.org' % (tag.title,)
    return render_to_response('articles/tag_view.html',
                              RequestContext(request, {'title': title, 'description': description,
                                                       'articles': articles, 'tag': tag}))


def article_page(request, topic, slug):
    article = get_object_or_404(Article, slug=slug)
    topic = article.topic.slug
    return render_to_response('articles/article_page.html',
                              RequestContext(request, {'title': article.title, 'description': article.teaser,
                                                       'article': article}))


def reviews_view(request):
    reviews_list = Review.objects.all()
    paginator = Paginator(reviews_list, 10)
    page = request.GET.get('page')
    try:
        reviews = paginator.page(page)
    except PageNotAnInteger:
        reviews = paginator.page(1)
    except EmptyPage:
        reviews = paginator.page(paginator.num_pages)
    title = 'Book & Product Reviews'
    description = 'Read recommendations and reviews of different books and products.'
    return render_to_response('articles/reviews_view.html',
                              RequestContext(request, {'title': title, 'description': description,
                                                       'reviews': reviews}))


def review_page(request, slug):
    review = get_object_or_404(Review, slug=slug)
    title = review.title
    description = review.description
    return render_to_response('articles/review_page.html',
                              RequestContext(request, {'title': title, 'description': description,
                                                       'review': review}))


def studies_view(request):
    studies_list = Study.objects.all()
    paginator = Paginator(studies_list, 10)
    page = request.GET.get('page')
    try:
        studies = paginator.page(page)
    except PageNotAnInteger:
        studies = paginator.page(1)
    except EmptyPage:
        studies = paginator.page(paginator.num_pages)
    title = 'In-Depth Studies'
    description = 'Read more in-depth studies on Restorus.org'
    return render_to_response('articles/studies_view.html',
                              RequestContext(request, {'title': title, 'description': description,
                                                       'studies': studies}))


def study_page(request, slug):
    study = get_object_or_404(Study, slug=slug)
    title = study.title
    description = study.description
    return render_to_response('articles/study_page.html',
                              RequestContext(request, {'title': title, 'description': description,
                                                       'study': study}))
