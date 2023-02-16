from django.urls import path,include
from .views import article_list,home1, article_detail,create_article
from . import views
urlpatterns = [
    path('articles/', article_list, name='article_list'),
    path('', home1, name='home'),
    path('articles/<int:pk>/', article_detail, name='article_detail'),
    path('articles/create/', views.create_article, name='create_article'),

]




