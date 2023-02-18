from django.shortcuts import render

from news.models import Img


def news_views(request):
    context = {'img': Img.objects.all() }
    return render(request, 'news/page_1.html', context)
