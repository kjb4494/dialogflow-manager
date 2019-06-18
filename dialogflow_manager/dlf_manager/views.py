from django.shortcuts import render
from django.http import HttpResponseRedirect
from .libs import intents_mng
from .decorators import requires_login
from . import errors


# Create your views here.
def index(request):
    return render(request, 'index.html')


@requires_login
def intents(request):
    return render(request, 'intents.html')


@requires_login
def entities(request):
    return render(request, 'entities.html')


@requires_login
def test(request):
    return render(request, 'test.html')


@requires_login
def intents_sync(request):
    ref = request.META.get('HTTP_REFERER')
    if ref is None:
        return errors.bad_requests(request)
    intents_mng.get_all_intents()
    return HttpResponseRedirect(ref)


@requires_login
def entities_sync(request):
    ref = request.META.get('HTTP_REFERER')
    if ref is None:
        return errors.bad_requests(request)
    return HttpResponseRedirect(ref)
