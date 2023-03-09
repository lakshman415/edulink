from django.shortcuts import render,redirect
from .forms import ArticleForm

# Create your views here.
from django.shortcuts import render
from .models import Article

def article_list(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'articles.html', context)

def article_detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {'article': article}
    return render(request, 'article_detail.html', context)

# def home1(request):
#     articles = Article.objects.all()
#     context = {'articles': articles}
#     return render(request, 'articles.html', context)

def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('article_list')
    else:
        form = ArticleForm()
    context = {'form': form}
    return render(request, 'create_article.html', context)

