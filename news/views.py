from django.shortcuts import render, get_object_or_404

from news.forms import CommentForm
from news.models import Img


def news_views(request):
    context = {'imgs': Img.objects.all() }
    return render(request, 'news/page_1.html', context)


def news_detail_view(request, img_id):
    detail = get_object_or_404(Img, id=img_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            form.save()
            form = CommentForm()

    else:
        form = CommentForm()

    comment = detail.comments.all()
    context = {'img_detail': detail, 'comments': comment, 'form': form}
    return render(request, 'news/details.html', context)



