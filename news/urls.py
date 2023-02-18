from django.urls import path

from news.views import news_views, news_detail_view

app_name = 'news'
urlpatterns = [
    path('post/<int:img_id>/', news_detail_view, name='detail'),
    path('', news_views, name='img'),


]

