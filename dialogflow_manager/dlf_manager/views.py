from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Intents
from .libs import intents_mng
from .decorators import requires_login
from . import errors


# Create your views here.
def index(request):
    return render(request, 'index.html')


@requires_login
def intents(request):
    values = Intents.objects.all()
    context = {'intents': values}
    return render(request, 'intents.html', context)


@requires_login
def entities(request):
    return render(request, 'entities.html')


@requires_login
def test(request):
    values = Intents.objects.all()
    context = {'intents': values}
    return render(request, 'test.html', context)


@requires_login
def intents_sync(request):
    ref = request.META.get('HTTP_REFERER')
    if ref is None:
        return errors.bad_requests(request)
    intents_mng.dlf_and_localdb_sync()
    return HttpResponseRedirect(ref)


@requires_login
def entities_sync(request):
    ref = request.META.get('HTTP_REFERER')
    if ref is None:
        return errors.bad_requests(request)
    return HttpResponseRedirect(ref)
