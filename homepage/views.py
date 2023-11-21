from django.shortcuts import render

from .containers import container


def homepage(request):
    return render(
        request,
        'homepage/home.html',
        {
            'title': container.homepage_title,
            'homepage_urls': container.homepage_urls,
        }
    )
