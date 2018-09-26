from django.shortcuts import render
from . import models

# Create your views here.


def index(request):
    articles = models.Article.objects.all()
    return render(request, "testblog/index.html",{"articles": articles})

def article_page(request, article_id):
    article = models.Article.objects.get(pk = article_id)
    return render(request, "testblog/article_page.html", {"article": article})

def article_edit(request, article_id):
    if article_id == 0:
        return render(request, "testblog/article_edit.html")
    article = models.Article.objects.get(pk = article_id)
    return render(request, "testblog/article_edit.html",{"article": article})

def article_finish(request):
    title = request.POST.get('title', 'TITLE')
    content = request.POST.get('content', 'CONTENT')
    id = request.POST.get('id', 0)
    if id == '0':
        models.Article.objects.create(title=title, content=content)
    else:
        article = models.Article.objects.get(pk = id)
        article.title = title
        article.content = content
        article.save()
    articles = models.Article.objects.all()
    return render(request, "testblog/index.html",{"articles": articles})

