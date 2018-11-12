from django.shortcuts import render
from .services import Articles


def index(request):

    data = Articles.fetch_top_news()
    return render(request, 'news/index.html', data)


def hacker(request):
    data = Articles.fetch_hacker_news()
    return render(request, 'news/hacker.html', data)


def iq(request):
    data = Articles.fetch_iq()
    return render(request, 'news/index.html', data)


def nytbiz(request):
    data = Articles.fetch_nyt_biz()
    return render(request, 'news/index.html', data)
