from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')


def intents(request):
    return render(request, 'intents.html')


def entities(request):
    return render(request, 'entities.html')


def test(request):
    return render(request, 'test.html')
