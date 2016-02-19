from django.shortcuts import render_to_response, RequestContext, get_object_or_404

from dictionary.models import Definition


def dictionary_view(request):
    defs = Definition.objects
    a = defs.filter(slug__startswith='a')
    b = defs.filter(slug__startswith='b')
    c = defs.filter(slug__startswith='c')
    d = defs.filter(slug__startswith='d')
    e = defs.filter(slug__startswith='e')
    f = defs.filter(slug__startswith='f')
    g = defs.filter(slug__startswith='g')
    h = defs.filter(slug__startswith='h')
    i = defs.filter(slug__startswith='i')
    j = defs.filter(slug__startswith='j')
    k = defs.filter(slug__startswith='k')
    ell = defs.filter(slug__startswith='l')
    m = defs.filter(slug__startswith='m')
    n = defs.filter(slug__startswith='n')
    oh = defs.filter(slug__startswith='o')
    p = defs.filter(slug__startswith='p')
    q = defs.filter(slug__startswith='q')
    r = defs.filter(slug__startswith='r')
    s = defs.filter(slug__startswith='s')
    t = defs.filter(slug__startswith='t')
    u = defs.filter(slug__startswith='u')
    v = defs.filter(slug__startswith='v')
    w = defs.filter(slug__startswith='w')
    x = defs.filter(slug__startswith='x')
    y = defs.filter(slug__startswith='y')
    z = defs.filter(slug__startswith='z')
    title = 'Political Dictionary'
    description = 'Access Restorus.org\'s political dictionary to define important terms.'
    return render_to_response('dictionary/dictionary_view.html',
                              RequestContext(request, {'title': title, 'description': description,
                                                       'a': a, 'b': b, 'c': c, 'd': d, 'e': e, 'f': f,
                                                       'g': g, 'h': h, 'i': i, 'j': j, 'k': k, 'ell': ell,
                                                       'm': m, 'n': n, 'oh': oh, 'p': p, 'q': q, 'r': r,
                                                       's': s, 't': t, 'u': u, 'v': v, 'w': w, 'x': x,
                                                       'y': y, 'z': z}))


def definition_view(request, slug):
    definition = get_object_or_404(Definition, slug=slug)
    title = 'Define %s' % (definition.title,)
    description = 'Define %s and other terms on Restorus.org' % (definition.title,)
    return render_to_response('dictionary/definition_view.html',
                              RequestContext(request, {'title': title, 'description': description,
                                                       'definition': definition}))
