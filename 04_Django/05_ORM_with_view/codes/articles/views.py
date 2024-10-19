from django.shortcuts import render, redirect
# 모델 클래스 가져오기
from .models import Article

# Create your views here.
def index(request):
    # 게시글 전체 조회 요청 to DB
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    # url로부터 전달받은 pk를 활용해 데이터를 조회
    # 앞의 pk는 기본키를 의미하고, 뒤의 pk는 전달받은 pk이다.
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


def new(request):
    # 게시글 작성 페이지 응답
    return render(request, 'articles/new.html')


def create(request):
    # 1. 사용자 요청으로부터 입력 데이터 추출
    title = request.POST.get('title')
    content = request.POST.get('content')

    # 저장 1.
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    # 저장 2.
    article = Article(title=title, content=content)
    article.save()

    # 저장 3.
    # Article.objects.create(title=title, content=content)

    # return redirect('articles:index')
    return redirect('articles:detail', article.pk)


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')


def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/edit.html', context)