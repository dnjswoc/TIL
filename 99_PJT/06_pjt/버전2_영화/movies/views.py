from django.shortcuts import render,redirect
from .models import Movie, Comment
from .forms import CreateForm, CommentForm
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods


# Create your views here.


def index(request):
    movies = Movie.objects.all()
    context = {
        'movies' : movies,
    }
    return render(request, 'movies/index.html',context)



@login_required
def create(request):
    if request.method=="POST":
        form = CreateForm(request.POST)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.user = request.user
            movie.save()
            return redirect('movies:index')
    else:
        form = CreateForm()
    context = {
        'form': form,
    }
    return render(request, 'movies/create.html', context)


def detail(request, movie_pk):
    movie = Movie.objects.get(pk = movie_pk)
    comment_form = CommentForm()
    comments = Comment.objects.all()
    context = {
        'movie' : movie,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'movies/detail.html', context)



@login_required
def update(request,movie_pk):
    movie = Movie.objects.get(pk = movie_pk)
    if request.method == 'POST':
        form = CreateForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movies:detail', movie.pk)

    else:
        form = CreateForm(instance=movie)
    context ={
        'form' : form,
        'movie' : movie,
    }
    return render(request, 'movies/update.html',context)


@login_required
def delete(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    movie.delete()
    return redirect('movies:index')


@login_required
def likes(request, movie_pk):
    movie = Movie.objects.get(pk = movie_pk)
    if request.user in movie.like_users.all():
        movie.like_users.remove(request.user)
    else:
        movie.like_users.add(request.user)
    return redirect('movies:index')



@login_required
def comments_create(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.movie = movie
            comment.user = request.user
            comment.save()
            return redirect('movies:detail', movie.pk)
    context = {
        'movie': movie,
        'comment_form': comment_form,
    }
    return render(request, 'movies/index.html', context)


@login_required
def comments_delete(request, movie_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('movies:detail', movie_pk)