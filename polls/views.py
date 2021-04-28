from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Article

def index(request):
    articles = Article.objects.all()
    context = {
        'message': 'Welcome my BBS',
        'articles': articles,
    }
    return render(request, 'polls/index.html', context)

def detail(request, id):
    article = get_object_or_404(Article, pk=id)
    context = {
        'message' : 'Show article' + str(id),
        'article' : article,
    }
    return render(request, 'polls/detail.html', context)