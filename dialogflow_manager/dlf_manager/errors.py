from django.shortcuts import render


def bad_requests(request):
    res = render(request, 'errorPages/400.html')
    res.status_code = 400
    return res
