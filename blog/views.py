from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Article

def article_list(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'home.html', context)

def article_detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {'article': article}
    return render(request, 'article_detail.html', context)

def home1(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'articles.html', context)