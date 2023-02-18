from django.urls import path

from news.views import news_views

app_name = 'news'
urlpatterns = [
    path('', news_views, name='img')
    

]

