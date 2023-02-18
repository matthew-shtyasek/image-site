from django.shortcuts import render, get_object_or_404

from news.models import Img


def news_views(request):
    context = {'imgs': Img.objects.all() }
    return render(request, 'news/page_1.html', context)


def news_detail_view(request, img_id):
    detail = get_object_or_404(Img, id=img_id)
    context = {'img_detail': detail}
    return render(request, 'news/details.html', context)