from django.urls import path
from .views import article_list,article_detail,create_article

urlpatterns = [
    path('articles/', article_list, name='article_list'),
    # path('', home1, name='home'),
    path('articles/<int:pk>/', article_detail, name='article_detail'),
    path('articles/create/',create_article, name='create_article'),

]




