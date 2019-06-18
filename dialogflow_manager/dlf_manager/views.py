from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import errors


# Create your views here.
def index(request):
    return render(request, 'index.html')


def intents(request):
    return render(request, 'intents.html')


def entities(request):
    return render(request, 'entities.html')


def test(request):
    return render(request, 'test.html')


def intents_sync(request):
    ref = request.META.get('HTTP_REFERER')
    if ref is None:
        return errors.bad_requests(request)
    return HttpResponseRedirect(ref)


def entities_sync(request):
    ref = request.META.get('HTTP_REFERER')
    if ref is None:
        return errors.bad_requests(request)
    return HttpResponseRedirect(ref)
