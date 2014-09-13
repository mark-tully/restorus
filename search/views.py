from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from search.forms import SearchForm
from articles.models import Article


def search_page(request):
    articles = []
    show_results = False
    form = SearchForm()
    if request.GET.has_key('q'):
        show_results = True
        query = request.GET['q'].strip()
        if query:
            form = SearchForm({'q': query})
            articles_list = Article.objects.search(query,
                                                    fields=('title', 'teaser',
                                                            'body'))
            paginator = Paginator(articles_list, 10)
            page = request.GET.get('page')
            try:
                articles = paginator.page(page)
            except PageNotAnInteger:
                articles = paginator.page(1)
            except EmptyPage:
                articles = paginator.page(paginator.num_pages)

    variables = RequestContext(request, {
        'form': form,
        'title': 'Search Articles on Restorus.org',
        'articles': articles,
        'show_results': show_results
    })
    return render_to_response('search/search_page.html', variables)