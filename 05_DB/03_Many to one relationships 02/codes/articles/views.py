from django.shortcuts import render, redirect
# 인증과 관련된 데코레이터
from django.contrib.auth.decorators import login_required
# HTTP를 위한 view함수에 사용할 데코레이터
from django.views.decorators.http import require_http_methods, require_POST

from .models import Article, Comment
from .forms import ArticleForm, CommentForm


def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

@login_required
def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    comments = article.comment_set.all()
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)


# require_http_methods 데코레이터가 없는 상황에서
# PUT/PATCH, DELETE 등의 메서드등의 요청이 들어오게 되면?
# 로직상, if 문으로 POST에 대해서만 조건분기를 해뒀고, 
# 나머지 (else) 그냥 HTML 반환 하는 형식으로 코드를 작성해 놨다.

# 반면, 데코레이터를 통해서 
# POST요청과 GET요청만 허용하게 해둔 상태에서 다른 메서드로 요청이 오면
# 그떄는 STATUS CODE 405 mtehod not allowed를 반환
@login_required
@require_http_methods(['POST', 'GET'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            # 게시글 생성을 위해, 넘겨받은 데이터로 생성 할 건데
            # 사용자가 넘겨준 데이터에는 user에 대한 정보는 form에 없다.
            # 그래서, 일단, 객체를 만들긴 할건데...
                # DB에 반영은 아직 하지 말아봐
            article = form.save(commit=False)
            # DB에는 반영되진 않앗지만... 사용자가 form으로 보낸
            # title, content를 포함한 article 객체가 만들어졌고,
            # 그 article 객체는 ArticleForm으로 만들어 졌으니,
                # class Meta의 model = Article을 적어 놨기 때문에
            # 내가 만든 models의 Article class의 인스턴스가 되겠다.
            # 그래서 article.user 정보에 요청보낸 user의 정보를 담는다.
            article.user = request.user
            article.save()  # DB에 반영
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


# 삭제는 POST요청만 허용 할 거임
@login_required
@require_POST
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    # 아무리 작성자라도... POST 요청일때만... 삭제 할 수 있어야 할 것 같은데
    # if request.method == 'POST':
    # 작성자만 게시글을 삭제 할 수 있는 상태
    if request.user == article.user:
        article.delete()
        return redirect('articles:index')
    return redirect('articles:detail', article.pk)


@login_required
def update(request, pk):
    # 이미 게시글과 User의 1:N 관계에 대한 정의는
    # model과 Form, 그리고 CREATE 로직에서 다 처리헀음.
    # udate는 수정 할 일 없음!
    article = Article.objects.get(pk=pk)
    # 단, 작성자 본인 인 경우에만 수정 할 수 있어야함.
        # admin     !=     viktor
    if article.user == request.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                form.save()
                return redirect('articles:detail', article.pk)
        else:
            form = ArticleForm(instance=article)
        context = {
            'article': article,
            'form': form,
        }
        return render(request, 'articles/update.html', context)
    else:
        return redirect('articles:detail', article.pk)


def comments_create(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        # 작성자 정보만 추가
        comment.user = request.user
        comment.save()
        return redirect('articles:detail', article.pk)
    context = {
        'article': article,
        'comment_form': comment_form,
    }
    return render(request, 'articles/detail.html', context)


def comments_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
    return redirect('articles:detail', article_pk)
